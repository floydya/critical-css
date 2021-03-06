"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from apps.critical.views import CriticalAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CriticalAPIView.as_view()),
] + staticfiles_urlpatterns()


API_VERSION = getattr(settings, 'API_VERSION', 1)
API_BASE_URL = f'api/v{API_VERSION}/'

urlpatterns += [
    path(f'{API_BASE_URL}', include('apps.auth.api.urls'))
]
