from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from housing.serializers.car_serializer import CarSerializer

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status


from housing.models.car_models import Car
from housing.services.car_service import CarService, CarData


# Import permissions
# Custom permissions
from housing.permissions import SecurityPermission

# Index page - temporary
def index(request):
    return render(request, 'housing/index.html')


# Create car
# @api_view(['POST'])
# def create_car(request):
#     car = CarSerializer(data=request.data)
#
#     if not car.is_valid():
#         return Response(car.errors)
#     car_data = CarData(**car.validated_data)
#     try:
#         car_service = CarService.create_car(car_data)
#         return Response(status=status.HTTP_201_CREATED)
#     except ValueError as e:
#         return Response(str(e))


# Test api for checking how tokens work
# Allows access only to security and admin
class TestView(APIView):
    permission_classes = (SecurityPermission,)
    def get(self, request):
        content = {'message': 'Ok!'}
        return Response(content)
