from rest_framework import serializers
from auth_client.models.messengers import Messengers


class MessengersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messengers
        fields = '__all__'

    def create(self, validated_data):
        return Messengers.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user_id_bot = validated_data.get('user_id_bot', instance.user_id_bot)
        instance.name_messenger = validated_data.get('name_messenger', instance.name_messenger)
        instance.bot_id = validated_data.get('bot_id', instance.bot_id)
        instance.save()
        return instance
