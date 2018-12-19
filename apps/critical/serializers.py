from django.conf import settings
from rest_framework import serializers

__all__ = ('CriticalSerializer',)


class CriticalSerializer(serializers.Serializer):
    css = serializers.URLField(help_text='Ссылка на .css файл.')
    url = serializers.URLField(help_text='Ссылка на веб-страницу.')
    width = serializers.IntegerField(
        default=1920, help_text='Ширина страницы. Стандартно: 1920.')
    height = serializers.IntegerField(
        default=100000, help_text='Высота страницы. Стандартно: 100000.')
    token = serializers.CharField(
        help_text='Secret token.'
    )

    def validate_token(self, value):
        if value != settings.SECRET_KEY:
            raise serializers.ValidationError('Token incorrect')
