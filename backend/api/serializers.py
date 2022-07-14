# todos/serializers.py
from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import Card


#Karten 
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

#Login 
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(
        label="Username",
        write_only=True
    )
    password = serializers.CharField(
        label="Password",
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            if not user:
                msg = 'Access denied: wrong username or password.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Both "username" and "password" are required.'
            raise serializers.ValidationError(msg, code='authorization')
        attrs['user'] = user
        return attrs
