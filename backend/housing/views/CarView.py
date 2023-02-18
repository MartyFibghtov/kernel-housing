from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from housing.models.car_models import Car
from housing.permissions import SecurityPermission
from housing.serializers.CarSerializer import CarSerializer
from housing.services.CarService import CarData, CarService



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def car_get_all(request):
    cars = Car.objects.all()
    serializer = CarSerializer(cars, many=True)

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def car_get_by_id(request):
    # Get id of car
    car_id = request.query_params.get('id')
    # If id not provided
    if not car_id:
        return Response({"error": "id is required in query parameters"})

    car = get_object_or_404(Car, pk=car_id)
    serializer = CarSerializer(car)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([SecurityPermission])
def car_create(request):
    # Has to be security or admin

    car = CarSerializer(data=request.data)

    if not car.is_valid():
        return Response(car.errors)
    car_data = CarData(**car.validated_data)
    try:
        car_service = CarService.create_car(car_data)
        return Response(status=status.HTTP_201_CREATED)
    except ValueError as e:
        return Response(str(e))
