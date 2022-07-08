# todos/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view()), # anmelden
    path('read/', views.ListCard.as_view()), #zeige die Karten --> /read
    path('add/', views.AddCard.as_view()), #Karte hinzufügen
    path('delete/<int:pk>/', views.DeleteCard.as_view()), 
    path('update/<int:pk>/', views.UpdateCard.as_view()),
]