from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse
from . import models
from .markdown_utils import render_markdown


def _breadcrumbs():
    return [("Courses", reverse("course_index"))]


def course_index(request):
    courses = models.Course.objects.all()
    context = {"courses": courses, "breadcrumbs": _breadcrumbs()}
    return render(request, "content_management/course_index.html", context=context)


def course_detail(request, course_id):
    course = get_object_or_404(models.Course, pk=course_id)
    breadcrumbs = _breadcrumbs() + [
        (course.title, reverse("course_detail", args=[course_id]))
    ]
    blurb = render_markdown(course.blurb, request)
    context = {"course": course, "breadcrumbs": breadcrumbs, "blurb": blurb}
    return render(request, "content_management/course_details.html", context=context)


def content_item_detail(request, course_id, content_item_position):
    """This will display a single content item"""
    course_content = get_object_or_404(
        models.CourseContent, course_id=course_id, position=content_item_position - 1
    )
    content_item = course_content.content_item

    if (
        content_item.visibility != content_item.PUBLIC
        and not request.user.is_authenticated
    ):
        messages.add_message(
            request,
            messages.WARNING,
            "You tried to access private content! Please sign up or sign in to see it",
        )
        return redirect(f"{reverse('account_login')}?next={request.path}")

    breadcrumbs = _breadcrumbs() + [
        (course_content.course.title, reverse("course_detail", args=[course_id])),
        (content_item.title, request.get_full_path()),
    ]

    content = render_markdown(content_item.content, request)

    context = {
        "content_item": content_item,
        "breadcrumbs": breadcrumbs,
        "content": content,
    }

    return render(
        request, "content_management/content_item_detail.html", context=context
    )
