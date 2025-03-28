from django.urls import path

from . import views

urlpatterns = [
    path("conversation/<str:name>", views.get_conversation, name="conversation"),
]
