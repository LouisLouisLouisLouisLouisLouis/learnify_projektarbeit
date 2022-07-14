from django.contrib.auth import login, logout
from rest_framework import status
from rest_framework import generics
from rest_framework import permissions
from rest_framework import views
from rest_framework.response import Response
from .models import Card
from .serializers import CardSerializer
from . import serializers



#login --> APIView
class LoginView(views.APIView):
    permission_classes = []
    authentication_classes = []

    def post(self, request, format=None):
        serializer = serializers.LoginSerializer(data=self.request.data,
            context={ 'request': self.request })
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response("true")

#read --> ListAPIView
class ListCard(generics.ListAPIView):
    permission_classes = []
    throttle_classes = []
    queryset = Card.objects.all()
    serializer_class = CardSerializer

#add --> UpdateAPIView
class AddCard(generics.CreateAPIView):
    permission_classes = [] 
    queryset = Card.objects.all()
    serializer_class = CardSerializer

#delete --> DestroyAPIView
class DeleteCard(generics.DestroyAPIView):
    permission_classes = []
    queryset = Card.objects.all()
    serializer_class = CardSerializer

#update --> UpdateAPIView
class UpdateCard(generics.UpdateAPIView):
    permission_classes = []
    throttle_classes = []
    queryset = Card.objects.all()
    serializer_class = CardSerializer


