from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .serializers import CriticalSerializer

__all__ = ('CriticalAPIView',)


class CriticalAPIView(CreateAPIView):
    """
    {
        "token":"rc-%i915$h_$2bsgp)+q3b(+7s)hn^1dptl+f4hbd8kzi3_jo*",
        "height":"100000",
        "width":"1920",
        "style":"http:\/\/mysite.loc\/style.css",
        "pages":[
            {
                "post_type":"works",
                "term_id":"",
                "post_id":"",
                "url":""
            },
            {
                "post_type":"",
                "term_id":"123",
                "post_id":"",
                "url":""
            }
            {
                "post_type":"",
                "term_id":"",
                "post_id":"123131",
                "url":""
            }
        ]
    }
    """
    serializer_class = CriticalSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'status': 'In process'})
