from rest_framework.generics import ListCreateAPIView, UpdateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from apps.application.api.serializers import ApplicationSerializer, TokenSerializer
from apps.application.models import Application


class ListCreateView(ListCreateAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Application.objects.all()

    def get_queryset(self):
        qs = super(ListCreateView, self).get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs


class RetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Application.objects.all()

    def get_queryset(self):
        qs = super(RetrieveUpdateDestroyView, self).get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs


class RegenerateTokenView(UpdateAPIView):
    serializer_class = TokenSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Application.objects.all()

    def get_queryset(self):
        qs = super(RegenerateTokenView, self).get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs
