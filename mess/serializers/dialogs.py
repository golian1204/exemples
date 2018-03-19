from rest_framework import serializers
from mess.models.dialogs import Dialogs, Messages, AutoAnswer, YesNoAnswer


class DialogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dialogs
        fields = '__all__'

    def create(self, validated_data):
        return Dialogs.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.subscriber = validated_data.get('subscriber', instance.subscriber)
        instance.save()
        return instance


class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = '__all__'

    def create(self, validated_data):
        return Messages.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.dialog = validated_data.get('dialog', instance.dialog)
        instance.user_sender = validated_data.get('user_sender', instance.user_sender)
        instance.text = validated_data.get('text', instance.text)
        instance.mess = validated_data.get('mess', instance.mess)
        instance.save()
        return instance


class AutoAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoAnswer
        fields = '__all__'

    def create(self, validated_data):
        return AutoAnswer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.key_word = validated_data.get('key_word', instance.key_word)
        instance.anti_word = validated_data.get('anti_word', instance.anti_word)
        instance.mess = validated_data.get('mess', instance.mess)
        instance.save()
        return instance


class YesNoAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = YesNoAnswer
        fields = '__all__'

    def create(self, validated_data):
        return YesNoAnswer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.mess = validated_data.get('mess', instance.mess)
        instance.yes = validated_data.get('yes', instance.yes)
        instance.no = validated_data.get('no', instance.no)
        instance.save()
        return instance
