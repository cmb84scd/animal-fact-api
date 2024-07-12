"""Urls for animal facts api."""

from django.urls import path

from . import views

urlpatterns = [
    path("", views.FactList.as_view()),
    path("<int:pk>/", views.FactDetail.as_view()),
]
