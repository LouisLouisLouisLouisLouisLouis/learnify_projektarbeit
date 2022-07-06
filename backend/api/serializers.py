# todos/serializers.py
from rest_framework import serializers
from .models import Card


class CardSerializer(serializers.ModelSerializer):
    _id = serializers.ReadOnlyField(source='id')
    class Meta:
        model = Card
        fields = [
            '_id',
            'quest',
            'answer',
        ]
        
    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['_id'] = str(repr['_id'])  
        return repr
