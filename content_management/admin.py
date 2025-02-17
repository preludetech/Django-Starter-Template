from . import models
from django.contrib import admin
from grappelli.forms import GrappelliSortableHiddenMixin
from django.contrib.auth import get_user_model

User = get_user_model()

# @admin.register(models.ContentItem)
# class ContentItemAdmin(admin.ModelAdmin):
#     pass


class CourseContentInline(GrappelliSortableHiddenMixin, admin.TabularInline):
    fields = ("content_item", "visibility", "position")
    model = models.CourseContent

    readonly_fields = ["visibility"]

    classes = ("grp-collapse grp-closed",)

    def visibility(self, obj):
        return obj.content_item.visibility


@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [CourseContentInline]


class CourseAccessInline(admin.TabularInline):
    model = models.CourseAccess
    readonly_fields = ["datetime_created"]


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    inlines = [CourseAccessInline]

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
