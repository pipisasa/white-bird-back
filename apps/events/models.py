from django.db import models

from uuid import uuid4


def generate_filename(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{str(uuid4())}.{ext}"
    return f"{filename}"


class Event(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to=generate_filename)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'