from django.urls import path

from apps.reqs.views import RequestModelAPIView


urlpatterns = [
    path('api/reqs/', RequestModelAPIView.as_view(), name="reqs"),
]
