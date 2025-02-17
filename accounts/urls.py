from django.urls import path
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    path(
        "profile/",
        # TemplateView.as_view(template_name="accounts/profile.html"),
        views.edit_profile,
        name="account_profile",
    ),
]
