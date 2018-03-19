from rest_framework import serializers
from subscriptions.models.subs_list import SubsList


class SubsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubsList
        fields = '__all__'

    def create(self, validated_data):
        return SubsList.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.user = validated_data.get('user', instance.user)
        instance.uuid = validated_data.get('uuid', instance.uuid)
        instance.deleted = validated_data.get('deleted', instance.deleted)
        instance.save()
        return instance
