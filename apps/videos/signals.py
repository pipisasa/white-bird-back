import os

from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import Video

from uuid import uuid4

import subprocess


@receiver(post_save, sender=Video)
def compress_video(sender, instance, created, **kwargs):
    if created:
        input_file = instance.video.path
        output_file = f'media/videos/{uuid4()}.mp4'
        subprocess.run(['ffmpeg', '-i', input_file, '-q:v', '4', output_file])
        instance.video.name = output_file.split('/')[-1]
        instance.save()
        os.remove(input_file)


@receiver(pre_delete, sender=Video)
def delete_video_file(sender, instance, **kwargs):
    if instance.video:
        if os.path.isfile(instance.video.path):
            os.remove(instance.video.path)
