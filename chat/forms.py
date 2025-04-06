from django import forms
from .models import Message


class ChatMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["message"]
        # widgets = {
        #     "message": forms.Textarea()
        # }
