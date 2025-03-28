from . import models
from django.contrib import admin
from django.contrib.auth import get_user_model
from unfold.admin import StackedInline, TabularInline
from taggit.managers import TaggableManager

from unfold.admin import ModelAdmin
from unfold import widgets
from taggit.forms import TagWidgetMixin


User = get_user_model()


@admin.register(models.ContentItem)
class ContentItemAdmin(ModelAdmin):
    pass


class CourseContentInline(TabularInline):
    model = models.CourseContent
    hide_title = True

    readonly_fields = [
        "visibility",
    ]

    classes = ("grp-collapse grp-closed",)

    ordering_field = "position"
    hide_ordering_field = True

    def visibility(self, obj):
        return obj.content_item.visibility


class UnfoldTaggitWidget(TagWidgetMixin, widgets.UnfoldAdminTextInputWidget):
    pass


@admin.register(models.Course)
class CourseAdmin(ModelAdmin):
    inlines = [CourseContentInline]

    formfield_overrides = {
        TaggableManager: {"widget": UnfoldTaggitWidget},
    }


class CourseAccessInline(TabularInline):
    model = models.CourseAccess
    readonly_fields = ["datetime_created"]


@admin.register(models.User)
class UserAdmin(ModelAdmin):
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
