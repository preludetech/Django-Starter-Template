from channels.generic.websocket import WebsocketConsumer
from .models import Conversation, Message
from django.template.loader import render_to_string
import json


class ConversationConsumer(WebsocketConsumer):
    def connect(self):

        self.user = self.scope["user"]
        conversation_name = self.scope["url_route"]["kwargs"]["name"]

        self.conversation = Conversation.objects.get(name=conversation_name)
        self.accept()

    def receive(self, text_data):
        data = json.loads(text_data)
        message_string = data["message"]
        message = Message.objects.create(
            message=message_string, conversation=self.conversation, from_user=self.user
        )

        print("message created")
        context = {"message": message, "user": self.user}
        html = render_to_string(
            "chat/conversation.html#hx-chat-bubble", context=context
        )
        self.send(text_data=html)
