from django.urls import path

from apps.reqs.views import RequestModelAPIView, RequestModelExportView


urlpatterns = [
    path('api/reqs/', RequestModelAPIView.as_view(), name="reqs"),
    # path('api/reqs/get-excel/', RequestModelExportView.as_view(), name='download-request-data'),
]
