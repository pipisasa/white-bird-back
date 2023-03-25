from rest_framework.routers import SimpleRouter

from .views import PostViewSet


router = SimpleRouter()

router.register('api/posts',PostViewSet, basename='api/posts')


urlpatterns = []
urlpatterns += router.urls
