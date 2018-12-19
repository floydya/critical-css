from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from .views import CriticalAPIView

urlpatterns = [
    path('', CriticalAPIView.as_view())
] + staticfiles_urlpatterns()
