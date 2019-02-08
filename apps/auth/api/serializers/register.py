from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers

__all__ = ("RegisterSerializer",)


class RegisterSerializer(serializers.ModelSerializer):

    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'confirm_password')

    def validate(self, attrs):
        username, email, password, confirm_password = attrs.values()

        if password != confirm_password:
            raise serializers.ValidationError(
                {
                    'password': _('Passwords are not equal.'),
                    'confirm_password': _('Passwords are not equal.')
                })

        try:
            User.objects.get(username=username)
            raise serializers.ValidationError({'username': _('User with this username already exists.')})
        except User.DoesNotExist:
            pass

        try:
            User.objects.get(email=email)
            raise serializers.ValidationError({'email': _('User with this email already exists.')})
        except User.DoesNotExist:
            pass

        return attrs

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        validated_data['is_active'] = True
        user = User.objects.create_user(**validated_data)
        return user
