"""App to notify for buses"""
from django.apps import AppConfig


class ViberConfig(AppConfig):
    """Viber app to notify

    Args:
        AppConfig (_type_): _description_
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "viber"
