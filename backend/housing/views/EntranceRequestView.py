import collections

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from housing.models.entrance_request_models import EntranceRequest
from housing.permissions import SecurityPermission
from housing.serializers.EntranceRequestSerializer import EntranceRequestSerializer
from housing.services.CarService import CarData
from housing.services.EntranceRequestService import EntranceRequestService, EntranceRequestData


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def entrance_request_get_all(request):
    cars = EntranceRequest.objects.all()
    serializer = EntranceRequestSerializer(cars, many=True)

    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def entrance_request_get_by_id(request):
    # Get id of car
    er_id = request.query_params.get('id')
    # If id not provided
    if not er_id:
        return Response({"error": "id is required in query parameters"})

    er = get_object_or_404(EntranceRequest, pk=er_id)
    serializer = EntranceRequestSerializer(er)

    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([SecurityPermission])
def entrance_request_create(request):
    er = EntranceRequestSerializer(data=request.data)

    if not er.is_valid():
        return Response(er.errors)
    validated_data: collections.OrderedDict = er.validated_data

    er_data = EntranceRequestData(car=CarData(**validated_data.pop('car')), **validated_data)
    try:
        er_service = EntranceRequestService.create_entrance_request(er_data)
    except ValueError as e:
        return Response({"error": str(e)})

    return Response(status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
@permission_classes([SecurityPermission])
def entrance_request_delete_by_id(request):
    # Get id of car
    er_id = request.query_params.get('id')
    # If id not provided
    if not er_id:
        return Response({"error": "id is required in query parameters"})
    try:
        er = EntranceRequest.objects.get(id=er_id).delete()
    except ObjectDoesNotExist as e:
        return Response({"error": 'Entrance request does not exist'})

    return Response(status=status.HTTP_200_OK)