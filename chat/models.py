from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class Conversation(models.Model):
    name = models.CharField(max_length=100, unique=True)

    users_online = models.ManyToManyField(
        User, related_name="online_in_conversations", blank=True
    )


class Message(models.Model):
    conversation = models.ForeignKey(
        Conversation, on_delete=models.PROTECT, related_name="messages"
    )
    from_user = models.ForeignKey(User, on_delete=models.PROTECT)
    message = models.TextField()
    created_datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_datetime"]
