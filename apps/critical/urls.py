from django.urls import path

from .views import CriticalAPIView

urlpatterns = [
    path('', CriticalAPIView.as_view())
]
