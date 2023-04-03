from django.db import models


class Video(models.Model):
    video = models.FileField(upload_to='videos/', max_length=255)

    def __str__(self):
        return str(self.video)

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'
