from rest_framework import serializers
from mess.models.feedback import Valuation


class ValuationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Valuation
        fields = '__all__'

    def create(self, validated_data):
        return Valuation.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.scale = validated_data.get('scale', instance.scale)
        instance.icon = validated_data.get('icon', instance.icon)
        instance.save()
        return instance
