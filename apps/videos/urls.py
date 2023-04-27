from django.urls import path

from .views import GalleryAPIView


urlpatterns = [
    path("api/gallery/", GalleryAPIView.as_view(), name="gallery-list"),
]
