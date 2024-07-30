"""Serialize the data in the Fact table."""

from rest_framework import serializers

from .models import Fact


class FactSerializer(serializers.ModelSerializer):
    """Serialize the data in the Fact table."""

    class Meta:
        """Serialize the data in the Fact table."""

        model = Fact
        fields = "__all__"
