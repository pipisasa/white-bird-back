from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Video
from .serializers import VideoSerializer


class VideoViewSet(ReadOnlyModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
