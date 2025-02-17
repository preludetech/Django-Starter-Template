from django.db import models


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

    # tags
    def __str__(self):
        return self.title


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
    position = models.PositiveSmallIntegerField("Position", null=True)

    class Meta:
        ordering = ["position"]
