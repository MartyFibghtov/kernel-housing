from rest_framework import serializers


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(allow_null=True, required=False)
    car_number = serializers.CharField(allow_null=True, required=False, max_length=9)
    car_type = serializers.CharField(allow_null=True, required=False)
    car_mark = serializers.CharField(allow_null=True, required=False)
    owner = serializers.CharField(allow_null=True, required=False)


# class CarSerializer(serializers.ModelSerializer):
#
# 	car_type = serializers.SlugRelatedField(read_only=True, slug_field="name")
# 	car_mark = serializers.SlugRelatedField(read_only=True, slug_field="name")
# 	owner = PersonalAccountSerializer(many=False)
#
# 	class Meta:
# 		model = Car
# 		fields = ['car_number', 'owner', 'car_mark', 'car_type']

class CarTypeSerializer(serializers.Serializer):
    id = serializers.IntegerField(allow_null=True, required=False)
    name = serializers.CharField(allow_null=True, required=False)


class CarMarkSerializer(serializers.Serializer):
    id = serializers.IntegerField(allow_null=True, required=False)
    name = serializers.CharField(allow_null=True, required=False)