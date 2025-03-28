from django.shortcuts import render
from . import models


def get_conversation(request, name):
    conversation, _ = models.Conversation.objects.get_or_create(name=name)

    messages = conversation.messages.all()[:20]
    context = {"messages": messages}
    return render(request, "chat/conversation.html")
