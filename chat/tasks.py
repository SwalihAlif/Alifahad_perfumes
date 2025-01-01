# tasks.py
import django_rq
from .models import ChatRoom, ChatMessage
from django.contrib.auth.models import User

def create_chat_message(room_name, user_id, message):
    room = ChatRoom.objects.get(name=room_name)
    user = User.objects.get(id=user_id)
    return ChatMessage.objects.create(room=room, user=user, message=message)

# Enqueue the task
def enqueue_create_chat_message(room_name, user_id, message):
    queue = django_rq.get_queue('default')
    queue.enqueue(create_chat_message, room_name, user_id, message)

