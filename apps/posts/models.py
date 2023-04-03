from django.db import models

from uuid import uuid4


def generate_filename(instance, filename):
    ext = filename.split(".")[-1]
    filename = f"{str(uuid4())}.{ext}"
    return f"{filename}"


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="Новость")
    content = models.TextField(verbose_name="Содержание поста")
    img = models.ImageField(
        verbose_name="Картинка", 
        blank=True, 
        null=True, 
        upload_to=generate_filename
    )
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    date_updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
