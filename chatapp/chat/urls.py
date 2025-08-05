from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Add this line
    path('<str:room_name>/', views.room, name='room'),
]
