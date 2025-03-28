from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth import get_user_model

User = get_user_model()


class Course(models.Model):
    title = models.CharField(max_length=300)

    blurb = models.TextField()

    BEGINNER = "BEGINNER"
    INTERMEDIATE = "INTERMEDIATE"

    LEVEL_CHOICES = [
        (BEGINNER, BEGINNER),
        (INTERMEDIATE, INTERMEDIATE),
    ]
    level = models.CharField(choices=LEVEL_CHOICES, max_length=12)

    tags = TaggableManager()

    def __str__(self):
        return self.title

    def content_items(self):
        content = [
            o.content_item
            for o in self.content.order_by("position").prefetch_related("content_item")
        ]
        return content


class ContentItem(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()

    PUBLIC = "PUBLIC"
    LOGIN = "LOGIN"
    PAID = "PAID"

    VISIBILITY_CHOICES = [(PUBLIC, PUBLIC), (LOGIN, LOGIN), (PAID, PAID)]
    visibility = models.CharField(
        max_length=6, choices=VISIBILITY_CHOICES, default=PAID
    )

    def __str__(self):
        return self.title


class CourseContent(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="content")
    content_item = models.ForeignKey(
        ContentItem, on_delete=models.CASCADE, related_name="course_order"
    )
    position = models.PositiveSmallIntegerField("Position", null=True, default=1)

    class Meta:
        ordering = ["position"]


class CourseAccess(models.Model):
    datetime_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
