import os
import subprocess

from uuid import uuid4

from django.conf import settings
from django.db import models


def compress_video(instance, filename):
    input_path = instance.video.path
    output_path = os.path.join(
        settings.MEDIA_ROOT, "videos", str(uuid4()) + ".mp4"
    )

    # определяем аргументы для сжатия видео с помощью FFmpeg
    # здесь используются некоторые распространенные настройки, но вы можете настроить их по своему усмотрению
    command = [
        "ffmpeg",
        "-i",
        input_path,
        "-c:v",
        "libx264",
        "-preset",
        "slow",
        "-crf",
        "23",
        "-c:a",
        "aac",
        "-b:a",
        "128k",
        "-movflags",
        "+faststart",
        "-y",
        output_path,
    ]

    # запускаем процесс сжатия видео
    subprocess.call(command)

    # возвращаем относительный путь к сжатому видео
    return os.path.join("videos", os.path.basename(output_path))


class Video(models.Model):
    video = models.FileField(upload_to=compress_video)

    def __str__(self):
        return str(self.video)
