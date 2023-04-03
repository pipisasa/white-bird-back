from django.db import models


ROLE_CHOICES = (
    ("Participant", "участник"), 
    ("Viewer", "зритель")
)


class RequestModel(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="ФИО")
    country = models.CharField(max_length=255, verbose_name="Страна")
    city = models.CharField(max_length=255, verbose_name='Город')
    email = models.EmailField(max_length=219, verbose_name="Электронная почта")
    phone_number = models.CharField(
        max_length=20,
        verbose_name="номер телефона",
        help_text="Enter phone number in international format",
        unique=True,
        db_index=True
    )
    date_created = models.DateTimeField(auto_now_add=True)
    role = models.CharField(choices=ROLE_CHOICES, max_length=12, verbose_name="Роль")

    def __str__(self):
        return f"Заявка от {self.full_name}  -  {self.email}  -  {self.phone_number}"

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
