from django.apps import AppConfig


class VideosConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.videos"
    verbose_name = "Галерея"

    def ready(self):
        from apps.videos import signals
