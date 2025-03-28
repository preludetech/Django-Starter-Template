from django.contrib import admin
from django.urls import path
from unfold.admin import ModelAdmin
from .models import X
from . import views
from taggit.models import Tag


@admin.register(X)
class CustomAdmin(ModelAdmin):
    def get_urls(self):
        dashboard_view = self.admin_site.admin_view(
            views.Dashboard.as_view(model_admin=self)
        )

        return super().get_urls() + [
            path("dashboard", dashboard_view, name="dashboard"),
        ]


admin.site.unregister(Tag)


@admin.register(Tag)
class GroupAdmin(ModelAdmin):
    pass
