from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import CriticalSerializer

__all__ = ('CriticalAPIView',)


class CriticalAPIView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = CriticalSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'status': 'In process'})

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('auth:login')
        return render(request, template_name='index.jinja')
