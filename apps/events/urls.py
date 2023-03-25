from rest_framework.routers import SimpleRouter

from apps.events.views import EventViewSet


router = SimpleRouter()

router.register("api/events", EventViewSet, basename="events")

urlpatterns = []
urlpatterns += router.urls
