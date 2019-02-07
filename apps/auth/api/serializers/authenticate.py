from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers

__all__ = ("LoginSerializer",)


class LoginSerializer(serializers.ModelSerializer):

    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'password')

    def validate(self, attrs):
        username, password = attrs.get('username'), attrs.get('password')
        self.temp_user = authenticate(
            self.context['request'], username=username, password=password
        )
        if self.temp_user is None:
            raise serializers.ValidationError(_("Login or/and password are incorrect."))

        if not self.temp_user.is_active:
            raise serializers.ValidationError(_("User is not activated."))

        return attrs
