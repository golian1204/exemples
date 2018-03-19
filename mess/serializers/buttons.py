from rest_framework import serializers
from mess.models.buttons import LinkButton, Payment


class LinkButtonSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkButton
        fields = '__all__'

    def create(self, validated_data):
        return LinkButton.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.link = validated_data.get('link', instance.link)
        instance.save()
        return instance


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

    def create(self, validated_data):
        return Payment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.save()
        return instance
