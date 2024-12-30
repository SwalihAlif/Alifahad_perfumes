from django.shortcuts import render, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import ChatRoom, ChatMessage
from .tasks import enqueue_create_chat_message

@login_required
def chat_room(request, room_name):
    admin_user = request.user
    room, created = ChatRoom.objects.get_or_create(name=room_name, defaults={'admin': admin_user})

    # messages = room.messages.all()
    messages = room.messages.select_related('user').all()
    return render(request, 'user/room.html', {'room_name': room_name, 'messages': messages})

@staff_member_required
def admin_room_list(request):
    rooms = ChatRoom.objects.all()
    context = {'rooms': rooms}
    return render(request, 'admin/admin_rooms_list.html', context)



@staff_member_required
def admin_room_chat(request, room_id):
    room = get_object_or_404(ChatRoom, id=room_id)
    # messages = room.messages.all()
    messages = room.messages.select_related('user').all()

    if request.method == "POST":
        reply_message = request.POST.get("reply_message")
        admin_user = request.user  # Use the logged-in admin user
        ChatMessage.objects.create(room=room, user=admin_user, message=reply_message)
        enqueue_create_chat_message(room.name, admin_user.id, reply_message)
        return JsonResponse({'status': 'success', 'message': 'Reply sent successfully.'})

    context = {'room': room, 'messages': messages}
    return render(request, 'admin/admin_room_chat.html', context)


