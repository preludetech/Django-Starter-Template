from django.urls import path

from . import views

urlpatterns = [
    path("", views.course_index, name="course_index"),
    path("<int:course_id>", views.course_detail, name="course_detail"),
    path(
        "<int:course_id>/content/<int:content_item_position>/",
        views.content_item_detail,
        name="content_item_detail",
    ),
]
