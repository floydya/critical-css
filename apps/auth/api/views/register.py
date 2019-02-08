from django.contrib.auth import login as _login
from django.shortcuts import render, redirect

from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.auth.api.serializers import RegisterSerializer


__all__ = ("RegisterView",)


class RegisterView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, template_name='register.jinja')

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        _login(request, user)
        return Response({'status': 'OK'})
