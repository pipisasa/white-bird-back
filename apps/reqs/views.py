from rest_framework.generics import CreateAPIView

from apps.reqs.models import RequestModel
from apps.reqs.serializers import RequestModelSerializer


class RequestModelAPIView(CreateAPIView):
    queryset = RequestModel.objects.all()
    serializer_class = RequestModelSerializer
