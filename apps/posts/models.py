from django.db import models
from cloudinary.models import CloudinaryField


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название анонса")
    content = models.TextField(verbose_name="Содержание")
    img = CloudinaryField(
        'image',
        blank=True,
        null=True,
    )
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    date_updated = models.DateTimeField(
        auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Анонс'
        verbose_name_plural = 'Анонсы'
