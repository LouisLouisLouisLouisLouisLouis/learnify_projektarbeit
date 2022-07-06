# todos/urls.py
from django.urls import path
from . import views

urlpatterns = [
    #path('', views.ListCard.as_view()), #login screen?
    #path('login/', views.login.as_view()), #menü screen?
    path('read/', views.ListCard.as_view()), #zeige die Karten --> /read
    path('add/', views.AddCard.as_view()), #Karte hinzufügen
    path('delete/', views.DeleteCard.as_view()), 
    path('update/', views.UpdateCard.as_view()),
]