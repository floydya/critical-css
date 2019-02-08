from django.urls import path, include
from apps.application.api.views import (
    ListCreateView, RetrieveUpdateDestroyView, RegenerateTokenView
)

app_name = 'application'

urlpatterns = [
    path('apps/', include([
        path('', ListCreateView.as_view(), name='lc'),
        path('<pk>/', include([
            path('', RetrieveUpdateDestroyView.as_view(), name='rud'),
            path('regenerate_token/', RegenerateTokenView.as_view(), name='rtoken'),
        ])),
    ])),
]
