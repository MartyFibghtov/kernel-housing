
from rest_framework import serializers

from housing.serializers.CarSerializer import CarSerializer


class EntranceRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField(allow_null=True, required=False)
    # TODO Implement humans
    request_account = serializers.CharField()
    date_created = serializers.CharField(allow_null=True, required=False)
    car = CarSerializer()
    is_car = serializers.BooleanField()
    is_paid = serializers.BooleanField(required=False)
    note = serializers.CharField(allow_null=True, required=False)