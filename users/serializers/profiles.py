from rest_framework import serializers
from users.models.profiles import Profiles


class ProfilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profiles
        fields = '__all__'

    def create(self, validated_data):
        return Profiles.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.hash = validated_data.get('hash', instance.hash)
        instance.role = validated_data.get('role', instance.role)
        instance.save()
        return instance
