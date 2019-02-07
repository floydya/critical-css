from django.contrib.auth.views import LogoutView
from django.urls import path

from apps.auth.api.views import LoginView

app_name = 'auth'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
