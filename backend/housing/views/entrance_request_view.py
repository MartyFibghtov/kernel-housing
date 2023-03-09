import collections
import pprint

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from housing.models.entrance_request_models import EntranceRequest
from housing.permissions import SecurityPermission
from housing.serializers.entrance_request_serializer import EntranceRequestSerializer

from django.http import HttpResponseBadRequest, JsonResponse, HttpResponseServerError, HttpResponseNotFound

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def entrance_request_get_all(request):
    er = EntranceRequest.objects.all()
    serializer = EntranceRequestSerializer(er, many=True)
    data = serializer.data

    return JsonResponse(data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def entrance_request_get_by_id(request):
    # Get id of car
    er_id = request.query_params.get('id')
    # If id not provided
    if not er_id:
        return HttpResponseBadRequest("Id is required in query parameters")

    # TODO Check how this works
    er = get_object_or_404(EntranceRequest, pk=er_id)
    serializer = EntranceRequestSerializer(er)

    return JsonResponse(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([SecurityPermission])
def entrance_request_create(request):
    er = EntranceRequestSerializer(data=request.data)
    if not er.is_valid():
        return HttpResponseBadRequest(er.errors)
    validated_data: collections.OrderedDict = er.validated_data

    er_data = EntranceRequest(**validated_data)
    try:
        # er_service = EntranceRequestService.create_entrance_request(er_data)
        er_data.save()
        response = JsonResponse(EntranceRequestSerializer(er_data).data, status=status.HTTP_200_OK)
    except ValueError as e:
        response = HttpResponseServerError(str(e))

    return response


@api_view(['DELETE'])
@permission_classes([SecurityPermission])
def entrance_request_delete_by_id(request):
    # Get id of car
    er_id = request.query_params.get('id')
    # If id not provided
    if not er_id:
        return HttpResponseBadRequest("id is required in query parameters")
    try:
        er = EntranceRequest.objects.get(id=er_id).delete()
    except ObjectDoesNotExist as e:
        return HttpResponseNotFound('Entrance request does not exist')

    return JsonResponse("ok", status=status.HTTP_200_OK)