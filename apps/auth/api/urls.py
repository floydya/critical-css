from django.contrib.auth.views import LogoutView
from django.urls import path, include

from apps.auth.api.views import LoginView, RegisterView

app_name = 'auth'

urlpatterns = [
    path('auth/', include([
        path('login/', LoginView.as_view(), name='login'),
        path('register/', RegisterView.as_view(), name='register'),
        path('logout/', LogoutView.as_view(), name='logout'),
    ])),
]
