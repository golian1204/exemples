from rest_framework import serializers
from mess.models.attachments import Images, Videos, Audios, Files


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'

    def create(self, validated_data):
        return Images.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.link = validated_data.get('link', instance.link)
        instance.name = validated_data.get('name', instance.name)
        instance.weight = validated_data.get('weight', instance.weight)
        instance.order = validated_data.get('order', instance.order)
        instance.save()
        return instance


class VideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = '__all__'

    def create(self, validated_data):
        return Videos.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.link = validated_data.get('link', instance.link)
        instance.name = validated_data.get('name', instance.name)
        instance.weight = validated_data.get('weight', instance.weight)
        instance.order = validated_data.get('order', instance.order)
        instance.save()
        return instance


class AudiosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audios
        fields = '__all__'

    def create(self, validated_data):
        return Audios.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.link = validated_data.get('link', instance.link)
        instance.name = validated_data.get('name', instance.name)
        instance.weight = validated_data.get('weight', instance.weight)
        instance.order = validated_data.get('order', instance.order)
        instance.save()
        return instance


class FilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files
        fields = '__all__'

    def create(self, validated_data):
        return Files.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.link = validated_data.get('link', instance.link)
        instance.name = validated_data.get('name', instance.name)
        instance.weight = validated_data.get('weight', instance.weight)
        instance.order = validated_data.get('order', instance.order)
        instance.save()
        return instance
