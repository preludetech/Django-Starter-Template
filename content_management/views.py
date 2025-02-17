from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages

from . import models


def course_index(request):
    courses = models.Course.objects.all()
    context = {"courses": courses}
    return render(request, "content_management/course_index.html", context=context)


def course_detail(request, course_id):
    course = get_object_or_404(models.Course, pk=course_id)
    context = {"course": course}
    return render(request, "content_management/course_details.html", context=context)


# def index(request):
#     """This will list out all the content items"""
#     content_items = models.ContentItem.objects.all()
#     if not request.user.is_authenticated:
#         content_items = content_items.filter(is_public=True)
#     context = {"content_items": content_items}

#     return render(request, "content_management/index.html", context=context)


def content_item_detail(request, content_item_id):
    """This will display a single content item"""
    content_item = get_object_or_404(models.ContentItem, pk=content_item_id)
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

    context = {"content_item": content_item}
    return render(request, "content_management/detail.html", context=context)
