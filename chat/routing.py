from django.urls import path
from .consumers import ConversationConsumer

websocket_urlpatterns = [
    path("ws/conversation/<str:name>", ConversationConsumer.as_asgi()),
]
