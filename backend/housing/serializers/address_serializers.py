from rest_framework import serializers

from housing.models.address_models import PersonalAccount


class PersonalAccountSerializer(serializers.ModelSerializer):
	phonenumber_set = serializers.StringRelatedField(many=True)

	class Meta:
		model = PersonalAccount
		fields = ['id', 'name', 'phonenumber_set', 'is_cooperative_member', 'access_forbidden_since', 'address_name']

class StreetSerializer(serializers.Serializer):
	id = serializers.IntegerField(allow_null=True, required=False)
	short_name = serializers.CharField(allow_null=True, required=False)
	full_name = serializers.CharField(allow_null=True, required=False)
