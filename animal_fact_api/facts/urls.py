"""Urls for animal facts api."""

from django.urls import path

from . import views

urlpatterns = [
    path("facts/", views.FactList.as_view()),
    path("facts/<int:pk>/", views.FactDetail.as_view()),
]
