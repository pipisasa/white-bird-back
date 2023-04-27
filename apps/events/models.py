from django.db import models
from cloudinary.models import CloudinaryField


class Event(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name="Описание")
    image = CloudinaryField(
        'image',
        blank=True,
        null=True
    )
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    date_updated = models.DateTimeField(
        auto_now=True, verbose_name="Дата обновления")

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'
