from rest_framework import serializers
from mess.models.polls import Answers, Interview


class InterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = '__all__'

    def create(self, validated_data):
        return Interview.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.title = validated_data.get('title', instance.title)
        instance.save()
        return instance


class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = '__all__'

    def create(self, validated_data):
        return Answers.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.interview = validated_data.get('interview', instance.interview)
        instance.title = validated_data.get('title', instance.title)
        instance.order = validated_data.get('order', instance.order)
        instance.save()
        return instance


