from django.conf import settings
from rest_framework import serializers

__all__ = ('CriticalSerializer',)


class CriticalSerializer(serializers.Serializer):
    css = serializers.URLField()
    url = serializers.URLField()
    width = serializers.IntegerField(default=1920)
    height = serializers.IntegerField(default=100000)
    token = serializers.CharField()

    def validate_token(self, value):
        if value != settings.SECRET_KEY:
            raise serializers.ValidationError('Token incorrect')
