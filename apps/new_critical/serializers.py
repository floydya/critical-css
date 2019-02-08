import requests

from rest_framework import serializers

from app.celery import get_critical_css
from apps.application.models import Application

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
    token = serializers.CharField(required=True, help_text='Secret token.')
    height = serializers.IntegerField(default=100000, help_text='Высота страницы. Стандартно: 100000.')
    width = serializers.IntegerField(default=1920, help_text='Ширина страницы. Стандартно: 1920.')
    pages = PageSerializer(many=True, required=True)

    def validate(self, attrs):
        try:
            self.config = Application.objects.get(token=attrs['token'])
        except Application.DoesNotExist:
            raise serializers.ValidationError({'token': 'Token incorrect'})

        try:
            response = requests.get(self.config.hook_url, timeout=2, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
                'Critical': attrs['token']
            })
            if response.status_code != 200:
                raise requests.ConnectionError
        except requests.ConnectionError:
            raise serializers.ValidationError({'hook': 'Invalid hook url. Edit it in control panel.'})

        return attrs

    def create(self, validated_data):

        for page in validated_data['pages']:
            get_critical_css.delay(
                self.config.style_url,
                page['url'],
                self.validated_data['width'],
                self.validated_data['height'],
                page['post_type'],
                page['term_id'],
                page['post_id'],
                self.config.hook_url,
                self.config.token
            )
        return object
