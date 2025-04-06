from django.urls import path

from . import views

urlpatterns = [
    path("conversation/<str:name>", views.get_conversation, name="conversation"),
    path(
        "conversation/<str:name>/send",
        views.conversation_send_message,
        name="conversation_send_message",
    ),
]
