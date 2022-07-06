# todos/serializers.py
from rest_framework import serializers
from .models import Card


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'quest',
            'answer',
        )
        model = Card