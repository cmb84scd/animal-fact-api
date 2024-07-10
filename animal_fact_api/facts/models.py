"""Database models for animal facts."""

from django.db import models


class Facts(models.Model):
    """Database model for animal facts."""

    animal = models.CharField(max_length=30)
    fact = models.TextField()
