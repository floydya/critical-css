import uuid

from rest_framework import serializers

from apps.application.models import Application


class ApplicationSerializer(serializers.ModelSerializer):

    id = serializers.ReadOnlyField()
    token = serializers.ReadOnlyField()

    class Meta:
        model = Application
        fields = ('id', 'name', 'hook_url', 'style_url', 'token')

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super(ApplicationSerializer, self).create(validated_data)


class TokenSerializer(serializers.ModelSerializer):

    token = serializers.ReadOnlyField()

    class Meta:
        model = Application
        fields = ('token',)

    def update(self, instance, validated_data):
        new_token = uuid.uuid4()
        instance.token = new_token
        instance.save(update_fields=['token'])
        return instance
