# from rest_framework import exceptions
from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

# from apps.application.models import Application
from .serializers import CriticalSerializer

__all__ = ('CriticalAPIView',)


class CriticalAPIView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = CriticalSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'status': 'In process'})

    def get(self, request, *args, **kwargs):
        return render(request, template_name='index.html')


class _CriticalAPIView(CreateAPIView):
    """
    JSON example: https://pastebin.com/p7nEEp7s
    """
    serializer_class = CriticalSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'status': 'In process'})


# class AuthCriticalAPIView(CreateAPIView):
#     """
#     JSON example: https://pastebin.com/p7nEEp7s
#     """
#     serializer_class = CriticalSerializer
#
#     def authenticate(self, request):
#         key = request.META.get('Authentication')
#         if not key:
#             return None
#
#         try:
#             key = key.partition(' ')[2]
#         except IndexError:
#             return None
#
#         try:
#             app = Application.objects.get(token=key)
#         except Application.DoesNotExist:
#             raise exceptions.AuthenticationFailed('No such application')
#
#         return app
#
#     def post(self, request, *args, **kwargs):
#         application = self.authenticate(request)
#         serializer = self.get_serializer(data=request.data, context={'application': application})
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'status': 'In process'})
