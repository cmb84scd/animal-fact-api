"""Config for animal facts app."""

from django.apps import AppConfig


class FactsConfig(AppConfig):
    """Config class for animal facts."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "facts"
