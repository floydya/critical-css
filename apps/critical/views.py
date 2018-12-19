from django.http import HttpResponse
from rest_framework.generics import CreateAPIView
from .serializers import CriticalSerializer
from .core import get_critical_css

__all__ = ('CriticalAPIView',)


class CriticalAPIView(CreateAPIView):
    """
    {
        "css": "http://568848.webcase.web.hosting-test.net/wp-content/themes/webcase/build/static/css/style.css",
        "url": "http://568848.webcase.web.hosting-test.net/uslugi/?amp",
        "token": "rc-%i915$h_$2bsgp)+q3b(+7s)hn^1dptl+f4hbd8kzi3_jo*",
        "height": 100000,
        "width": 1920
    }
    """
    serializer_class = CriticalSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data.pop('token')
        return HttpResponse(get_critical_css(**serializer.validated_data))
