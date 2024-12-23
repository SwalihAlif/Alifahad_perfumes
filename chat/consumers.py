# consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .tasks import enqueue_create_chat_message
import logging

logger = logging.getLogger(__name__)

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
        logger.info(f"WebSocket connected to room {self.room_name}")

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        logger.info(f"WebSocket disconnected from room {self.room_name}")

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        user = self.scope['user']

        if not user.is_authenticated:
            logger.warning("Unauthenticated user tried to send a message.")
            return

        logger.info(f"Received message: {message} from user: {user.username}")

        # Enqueue the RQ task
        enqueue_create_chat_message(self.room_name, user.id, message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user': user.username
            }
        )

    async def chat_message(self, event):
        message = event['message']
        user = event['user']
        await self.send(text_data=json.dumps({
            'message': message,
            'user': user
        }))


# celery -A alifahad_perfumes worker --loglevel=info
# daphne -p 8000 alifahad_perfumes.asgi:application
