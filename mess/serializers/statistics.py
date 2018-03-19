from rest_framework import serializers
from mess.models.statistics import YesNoStatistic


class YesNoStatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = YesNoStatistic
        fields = '__all__'

    def create(self, validated_data):
        return YesNoStatistic.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.mess = validated_data.get('mess', instance.mess)
        instance.subscriber = validated_data.get('subscriber', instance.subscriber)
        instance.yes = validated_data.get('yes', instance.yes)
        instance.save()
        return instance
