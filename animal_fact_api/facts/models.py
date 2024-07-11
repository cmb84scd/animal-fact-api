"""Database models for animal facts."""

from django.db import models


class Fact(models.Model):
    """Database model for animal facts."""

    animal = models.CharField(max_length=30)
    fact = models.TextField()

    def __str__(self) -> str:
        """Return database object as a string."""
        return f"{self.animal}: {self.fact}"
