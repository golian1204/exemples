from rest_framework import serializers
from subscriptions.models.subs_blank import SubsBlank


class SubsBlankSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubsBlank
        fields = '__all__'

    def create(self, validated_data):
        return SubsBlank.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.offer = validated_data.get('offer', instance.offer)
        instance.call_to_action = validated_data.get('call_to_action', instance.call_to_action)
        instance.telegram = validated_data.get('telegram', instance.telegram)
        instance.facebook = validated_data.get('facebook', instance.facebook)
        instance.viber = validated_data.get('viber', instance.viber)
        instance.subs_list = validated_data.get('subs_list', instance.subs_list)
        instance.image = validated_data.get('image', instance.image)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.timer_date = validated_data.get('timer_date', instance.timer_date)
        instance.local_time = validated_data.get('local_time', instance.local_time)
        instance.timer_interval = validated_data.get('timer_interval', instance.timer_interval)
        instance.right_now = validated_data.get('right_now', instance.right_now)
        instance.utp = validated_data.get('utp', instance.utp)
        instance.cta = validated_data.get('cta', instance.cta)
        instance.confidentiality = validated_data.get('confidentiality', instance.confidentiality)
        instance.user = validated_data.get('user', instance.user)
        instance.deleted = validated_data.get('deleted', instance.deleted)
        instance.save()
        return instance
