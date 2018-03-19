from rest_framework import serializers
from bots.models.bots import Bots, TokensTelegram, TokensViber, TokensFacebook


class BotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bots
        fields = '__all__'

    def create(self, validated_data):
        return Bots.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.name = validated_data.get('name', instance.name)
        instance.type_messenger = validated_data.get('type_messenger', instance.type_messenger)
        instance.save()
        return instance


class TokensTelegramSerializer(serializers.ModelSerializer):
    class Meta:
        model = TokensTelegram
        fields = '__all__'

    def create(self, validated_data):
        return TokensTelegram.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.bot = validated_data.get('bot', instance.bot)
        instance.token = validated_data.get('token', instance.token)
        instance.save()
        return instance


class TokensViberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TokensViber
        fields = '__all__'

    def create(self, validated_data):
        return TokensViber.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.bot = validated_data.get('bot', instance.bot)
        instance.token = validated_data.get('token', instance.token)
        instance.save()
        return instance


class TokensFacebookSerializer(serializers.ModelSerializer):
    class Meta:
        model = TokensFacebook
        fields = '__all__'

    def create(self, validated_data):
        return TokensFacebook.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.bot = validated_data.get('bot', instance.bot)
        instance.token = validated_data.get('token', instance.token)
        instance.verify_token = validated_data.get('verify_token', instance.verify_token)
        instance.id_page = validated_data.get('id_page', instance.id_page)
        instance.save()
        return instance
