"""Urls for animal facts api."""

from django.urls import path

from . import views

urlpatterns = [
    path("facts/all", views.FactList.as_view(), name="fact-list"),
    path("facts/<int:pk>/", views.FactDetail.as_view(), name="fact-detail"),
    path("facts/", views.FactDetail.as_view(), name="fact-random"),
]
