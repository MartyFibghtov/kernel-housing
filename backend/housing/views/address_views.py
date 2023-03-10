from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from housing.models.address_models import PersonalAccount, Street
from housing.serializers.address_serializers import PersonalAccountSerializer, StreetSerializer
from housing.views.wrap_responses import response_wrap


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def personal_account_get_all(request):
    p_accounts = PersonalAccount.objects.all()

    serializer = PersonalAccountSerializer(p_accounts, many=True)
    response = response_wrap(serializer.data)

    return Response(response)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def street_get_all(request):
    p_accounts = Street.objects.all()

    serializer = StreetSerializer(p_accounts, many=True)
    response = response_wrap(serializer.data)

    return Response(response)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def address_get_all(request):
    response = response_wrap(ok=False, message="NOT IMPLEMENTED")

    return Response(response)
