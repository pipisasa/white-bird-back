from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.events.models import Event
from apps.events.serializers  import EventSerializer


class EventViewSet(ReadOnlyModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
