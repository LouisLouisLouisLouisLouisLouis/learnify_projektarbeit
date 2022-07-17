# todos/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view()),
    path('read/', views.ListCard.as_view()), 
    path('add/', views.AddCard.as_view()), 
    path('delete/<int:pk>/', views.DeleteCard.as_view()), 
    path('update/<int:pk>/', views.UpdateCard.as_view()),
]