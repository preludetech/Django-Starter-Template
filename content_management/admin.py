from . import models
from django.contrib import admin
from grappelli.forms import GrappelliSortableHiddenMixin


@admin.register(models.ContentItem)
class ContentItemAdmin(admin.ModelAdmin):
    pass


class CourseContentInline(GrappelliSortableHiddenMixin, admin.TabularInline):
    fields = ("content_item", "visibility", "position")
    model = models.CourseContent

    readonly_fields = ["visibility"]

    def visibility(self, obj):
        return obj.content_item.visibility


@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [CourseContentInline]
