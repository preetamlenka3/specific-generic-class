from django.apps import AppConfig


class SpecificConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'specific'
