# todos/urls.py
from django.urls import path
from . import views

urlpatterns = [
    #path('login', views.Login.as_view()), #login screen?
    #path('login/', views.login.as_view()), #menü screen?
    path('read/', views.ListCard.as_view()), #zeige die Karten --> /read
    path('add/', views.AddCard.as_view()), #Karte hinzufügen
    path('delete/<int:pk>/', views.DeleteCard.as_view()), 
    path('update/<int:pk>/', views.UpdateCard.as_view()),
]