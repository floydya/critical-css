from django.contrib.auth import login as _login

from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from apps.auth.api.serializers import LoginSerializer


__all__ = ("LoginView",)


class LoginView(CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        _login(request, serializer.temp_user)
        return Response({'status': 'OK'})


