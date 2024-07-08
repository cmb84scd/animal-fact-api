"""Views for animal facts api."""

from django.http import HttpResponse


def index_view(request):
    """Index page of animal facts api."""
    return HttpResponse("Welcome to animal facts!")
