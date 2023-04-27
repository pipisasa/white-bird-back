from django.forms import model_to_dict
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Video, Image


class GalleryAPIView(APIView):
    def get(self, request, *args):
        images = Image.objects.all().order_by('-date_created')
        videos = Video.objects.all().order_by('-date_created')

        images_data = []
        for image in images:
            image_dict = model_to_dict(image)
            image_dict['img'] = image.img.url
            images_data.append(image_dict)

        videos_data = []
        for video in videos:
            video_dict = model_to_dict(video)
            video_dict['video'] = video.video.url
            videos_data.append(video_dict)

        data = {
            'images': images_data,
            'videos': videos_data
        }

        return Response({'gallery': data})
