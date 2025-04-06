from django.urls import path
from .consumers import ConversationConsumer

websocket_urlpatterns = [
    path(r"ws/conversation/<str:name>/", ConversationConsumer.as_asgi()),
]
