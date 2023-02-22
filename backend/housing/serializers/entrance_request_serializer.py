
from rest_framework import serializers

from housing.models.car_models import Car
from housing.models.entrance_request_models import EntranceRequest

#
# class EntranceRequestSerializer(serializers.Serializer):
#     id = serializers.IntegerField(allow_null=True, required=False)
#     # TODO Implement humans
#     request_account = serializers.CharField()
#     date_created = serializers.CharField(allow_null=True, required=False)
#     car = CarSerializer()
#     is_car = serializers.BooleanField()
#     is_paid = serializers.BooleanField(required=False)
#     note = serializers.CharField(allow_null=True, required=False)


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'car_mark', 'car_type', 'car_number')

class EntranceRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntranceRequest
        fields = '__all__'

