from django.db import models
from django.core.validators import RegexValidator


class RequestModel(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="ФИО")
    email = models.EmailField(max_length=219, verbose_name="Электронная почта")
    phone_number = models.CharField(
        max_length=20,
        verbose_name="Phone number",
        help_text="Enter phone number in international format",
        unique=True,
        db_index=True,
        validators=[
            RegexValidator(
                regex=r"^\+(?:[0-9] ?){6,14}[0-9]$",
                message='Phone number must be entered in the format: "+999999999". Up to 15 digits allowed.',
            )
        ],
    )
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Заявка от {self.full_name}-{self.email}-{self.phone_number}'

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
