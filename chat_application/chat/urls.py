from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.index, name='index'),
    path('join/', views.join_room, name='join_room'),
    path('<str:room_name>/', views.room, name='room'),
]