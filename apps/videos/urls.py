from rest_framework.routers import SimpleRouter

from .views import VideoViewSet


router = SimpleRouter()

router.register('api/videos', VideoViewSet, basename='api/videos')

urlpatterns = []
urlpatterns += router.urls
