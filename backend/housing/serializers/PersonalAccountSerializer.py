from rest_framework import serializers

from housing.models.AddressModels import PersonalAccount


class PersonalAccountSerializer(serializers.ModelSerializer):
	phonenumber_set = serializers.StringRelatedField(many=True)

	class Meta:
		model = PersonalAccount
		fields = ['name', 'phonenumber_set', 'is_cooperative_member', 'access_forbidden_since', '__str__']


