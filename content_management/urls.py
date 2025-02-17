from django.urls import path

from . import views

urlpatterns = [
    path("", views.course_index, name="course_index"),
    path("<int:course_id>", views.course_detail, name="course_detail"),
    # path(
    #     "content/<int:content_item_id>/", views.content_item_detail, name="content_item_detail"
    # ),
]
