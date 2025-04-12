from django.contrib import admin
from . import models

from unfold.admin import ModelAdmin
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(models.Article)
class ArticleAdmin(ModelAdmin):
    pass


@admin.register(User)
class UserAdmin(ModelAdmin):

    fieldsets = [
        (
            None,
            {
                "fields": [
                    "email",
                    "full_name",
                    "is_active",
                ],
            },
        ),
        (
            "Permission options",
            {
                "classes": ["grp-collapse grp-closed"],
                "fields": [
                    "is_staff",
                    "is_superuser",
                    "user_permissions",
                    "groups",
                ],
            },
        ),
    ]
    readonly_fields = ["last_login"]
