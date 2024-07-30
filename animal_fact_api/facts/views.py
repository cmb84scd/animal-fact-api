"""Views for animal facts api."""

from django.db.models.functions import Random
from rest_framework import generics
from rest_framework.response import Response

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

    def get(self, request, *args, **kwargs):
        """Get a specific or random fact."""
        if "pk" in kwargs:
            return self.retrieve(request, *args, **kwargs)
        else:
            random_record = Fact.objects.order_by(Random()).first()
            serializer = self.get_serializer(random_record)
            return Response(serializer.data)
