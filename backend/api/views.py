from rest_framework import generics
from .models import Card
from .serializers import CardSerializer
#from rest_framework.permissions import IsAdminUser       ----> falls mit login

#read --> ListAPIView
class ListCard(generics.ListAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

#add --> CreateAPIView
class AddCard(generics.CreateAPIView):
    permission_classes = [] #
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


