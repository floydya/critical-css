import requests

from django.conf import settings
from rest_framework import serializers

from app.celery import get_critical_css

__all__ = ('CriticalSerializer',)


class PageSerializer(serializers.Serializer):
    post_type = serializers.CharField(required=False, allow_blank=True)
    term_id = serializers.CharField(required=False, allow_blank=True)
    post_id = serializers.CharField(required=False, allow_blank=True)
    url = serializers.CharField(required=True)

    def validate(self, attrs):
        if not (
            attrs.get('post_type', None) or
            attrs.get('term_id', None) or
            attrs.get('post_id', None)
        ):
            raise serializers.ValidationError('post_type or term_id or post_id are empty.')
        try:
            status_code = requests.get(attrs['url'], timeout=2, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}).status_code
        except requests.ConnectionError:
            status_code = "@Connection error/timeout@"
        if status_code != 200:
            raise serializers.ValidationError({'url': f'Returned {status_code} response.'})
        return attrs


class CriticalSerializer(serializers.Serializer):
    hook = serializers.URLField(required=True, help_text='Hook URL')
    token = serializers.CharField(required=True, help_text='Secret token.')
    height = serializers.IntegerField(default=100000, help_text='Высота страницы. Стандартно: 100000.')
    width = serializers.IntegerField(default=1920, help_text='Ширина страницы. Стандартно: 1920.')
    style = serializers.URLField(required=True, help_text='Ссылка на .css файл.')
    pages = PageSerializer(many=True, required=True)

    def validate_hook(self, value):
        try:
            response = requests.get(value, timeout=2, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'})
            if response.status_code != 200:
                raise requests.ConnectionError
        except requests.ConnectionError:
            raise serializers.ValidationError({'hook': 'Invalid hook url'})
        return value

    def validate_token(self, value):
        if value != settings.SECRET_KEY:
            raise serializers.ValidationError('Token incorrect')
        return value

    def create(self, validated_data):
        for page in validated_data['pages']:
            get_critical_css.delay(
                self.validated_data['style'],
                page['url'],
                self.validated_data['width'],
                self.validated_data['height'],
                page['post_type'],
                page['term_id'],
                page['post_id'],
                validated_data['hook']
            )
        return object
