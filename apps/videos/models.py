from django.db import models

from cloudinary.models import CloudinaryField


class Video(models.Model):
    video = CloudinaryField(
        resource_type='video',
        format='mp4',
        max_length=255
    )
    video_compressed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.video)

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'


class Image(models.Model):
    img = CloudinaryField(
        "image",
        blank=False,
        null=False,
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.img)

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"
