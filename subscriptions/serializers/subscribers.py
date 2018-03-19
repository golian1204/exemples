from rest_framework import serializers
from subscriptions.models.subscribers import Subscribers, Subscriptions


class SubscribersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribers
        fields = '__all__'

    def create(self, validated_data):
        return Subscribers.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.bot_id = validated_data.get('bot_id', instance.bot_id)
        instance.name_messenger = validated_data.get('name_messenger', instance.name_messenger)
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.subscribed = validated_data.get('subscribed', instance.subscribed)
        instance.chat_bot = validated_data.get('chat_bot', instance.chat_bot)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.save()
        return instance


class SubscriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriptions
        fields = '__all__'

    def create(self, validated_data):
        return Subscriptions.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.subs_list = validated_data.get('subs_list', instance.subs_list)
        instance.subscriber = validated_data.get('subscriber', instance.subscriber)
        instance.deleted = validated_data.get('deleted', instance.deleted)
        instance.save()
        return instance
