# todos/serializers.py
from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import Card


#Karten 
class CardSerializer(serializers.ModelSerializer):
    _id = serializers.ReadOnlyField(source='id')    #id to _id
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
    """
    This serializer defines two fields for authentication:
      * username
      * password.
    It will try to authenticate the user with when validated.
    """
    username = serializers.CharField(
        label="Username",
        write_only=True
    )
    password = serializers.CharField(
        label="Password",
        # This will be used when the DRF browsable API is enabled
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )

    def validate(self, attrs):
        # Take username and password from request
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            # Try to authenticate the user using Django auth framework.
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            if not user:
                # If we don't have a regular user, raise a ValidationError
                msg = 'Access denied: wrong username or password.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Both "username" and "password" are required.'
            raise serializers.ValidationError(msg, code='authorization')
        # We have a valid user, put it in the serializer's validated_data.
        # It will be used in the view.
        attrs['user'] = user
        return attrs
