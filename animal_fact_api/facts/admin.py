"""Add facts to admin interface."""

from django.contrib import admin

from .models import Fact

admin.site.register(Fact)
