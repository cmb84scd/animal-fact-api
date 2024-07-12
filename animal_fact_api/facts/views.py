"""Views for animal facts api."""

from rest_framework import generics

from .models import Fact
from .serializers import FactSerializer


class FactList(generics.ListAPIView):
    """View all facts."""

    queryset = Fact.objects.all()
    serializer_class = FactSerializer


class FactDetail(generics.RetrieveAPIView):
    """View an individual fact."""

    queryset = Fact.objects.all()
    serializer_class = FactSerializer
