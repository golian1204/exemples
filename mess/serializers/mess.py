from rest_framework import serializers
from mess.models.mess import Mess, MessStatus


class MessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mess
        fields = '__all__'

    def create(self, validated_data):
        return Mess.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.text = validated_data.get('text', instance.text)
        instance.images = validated_data.get('images', instance.images)
        instance.videos = validated_data.get('videos', instance.videos)
        instance.audios = validated_data.get('audios', instance.audios)
        instance.files = validated_data.get('files', instance.files)
        instance.interview = validated_data.get('interview', instance.interview)
        instance.valuation = validated_data.get('valuation', instance.valuation)
        instance.yesno = validated_data.get('yesno', instance.yesno)
        instance.like = validated_data.get('like', instance.like)
        instance.invite = validated_data.get('invite', instance.invite)
        instance.telegram = validated_data.get('telegram', instance.telegram)
        instance.facebook = validated_data.get('facebook', instance.facebook)
        instance.viber = validated_data.get('viber', instance.viber)
        instance.link_button = validated_data.get('link_button', instance.link_button)
        instance.payment = validated_data.get('payment', instance.payment)
        instance.user = validated_data.get('user', instance.user)
        instance.draft = validated_data.get('draft', instance.draft)
        instance.time_before = validated_data.get('time_before', instance.time_before)
        instance.time_after = validated_data.get('time_after', instance.time_after)
        instance.subs_online = validated_data.get('subs_online', instance.subs_online)
        instance.deleted = validated_data.get('deleted', instance.deleted)
        instance.save()
        return instance


class MessStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessStatus
        fields = '__all__'

    def create(self, validated_data):
        return MessStatus.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.mess = validated_data.get('mess', instance.mess)
        instance.subscriber = validated_data.get('subscriber', instance.subscriber)
        instance.plan_send_date = validated_data.get('plan_send_date', instance.plan_send_date)
        instance.send_date = validated_data.get('send_date', instance.send_date)
        instance.delivery_date = validated_data.get('delivery_date', instance.delivery_date)
        instance.read_date = validated_data.get('read_date', instance.read_date)
        instance.action_date = validated_data.get('action_date', instance.action_date)
        instance.process_status = validated_data.get('process_status', instance.process_status)
        instance.save()
        return instance
