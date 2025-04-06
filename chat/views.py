from django.shortcuts import render
from . import models
from django.contrib.auth.decorators import login_required
from .forms import ChatMessageForm


@login_required
def get_conversation(request, name):
    conversation, _ = models.Conversation.objects.get_or_create(name=name)
    form = ChatMessageForm()
    messages = conversation.messages.all()[:20]
    context = {"messages": messages, "form": form, "conversation_name": name}
    return render(request, "chat/conversation.html", context=context)


@login_required
def conversation_send_message(request, name):
    conversation = models.Conversation.objects.get(name=name)
    if request.method == "POST":
        form = ChatMessageForm(request.POST)
        if form.is_valid:
            message = form.save(commit=False)
            message.from_user = request.user
            message.conversation = conversation
            message.save()
            context = {"message": message}
            return render(
                request, "chat/conversation.html#chat-bubble", context=context
            )
