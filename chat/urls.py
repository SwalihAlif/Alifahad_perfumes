from django.urls import path
from .views import chat_room, admin_room_list, admin_room_chat

app_name = 'chat'

urlpatterns = [
    path('<str:room_name>/', chat_room, name='room'),

    path('admin/chat/', admin_room_list, name='admin_room_list'),
    path('admin/chat/<int:room_id>/', admin_room_chat, name='admin_chat_room'),
]





