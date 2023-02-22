from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from housing.models.car_models import Car, CarType, CarMark
from housing.permissions import SecurityPermission
from housing.serializers.car_serializer import CarSerializer, CarTypeSerializer, CarMarkSerializer
from housing.services.car_service import CarData, CarService
from housing.views.wrap_responses import response_wrap


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def car_get_all(request):
    cars = Car.objects.all()
    serializer = CarSerializer(cars, many=True)
    response = response_wrap(serializer.data)

    return Response(response)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def car_get_by_id(request):
    # Get id of car
    car_id = request.query_params.get('id')
    # If id not provided
    if not car_id:
        return Response(response_wrap(ok=False, message="id is required in query parameters"))

    car = get_object_or_404(Car, pk=car_id)
    serializer = CarSerializer(car)
    response = response_wrap(serializer.data)

    return Response(response)


@api_view(['POST'])
@permission_classes([SecurityPermission])
def car_create(request):
    """Create a car and return new instance."""
    # Has to be security or admin

    in_car_serializer = CarSerializer(data=request.data)

    if not in_car_serializer.is_valid():
        return Response(response_wrap(ok=False, message=str(in_car_serializer.errors)))

    car_data = CarData(**in_car_serializer.validated_data)

    try:
        car: Car = CarService.create_car(car_data)
        serializer = CarSerializer(car)
        response = response_wrap(serializer.data)

    except ValueError as e:
        response = response_wrap(ok=False, message=str(e))

    return Response(response)


@api_view(['GET'])
@permission_classes([SecurityPermission])
def car_type_get_all(request):
    car_types = CarType.objects.all()
    serializer = CarTypeSerializer(car_types, many=True)

    response = response_wrap(serializer.data)

    return Response(response)


@api_view(['GET'])
@permission_classes([SecurityPermission])
def car_mark_get_all(request):
    car_marks = CarMark.objects.all()
    serializer = CarMarkSerializer(car_marks, many=True)
    response = response_wrap(serializer.data)

    return Response(response)

