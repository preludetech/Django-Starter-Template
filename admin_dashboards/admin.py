from django.contrib import admin

# Register your models here.
from django.urls import path
from django.views.generic import TemplateView

from unfold.admin import ModelAdmin
from unfold.views import UnfoldModelAdminViewMixin
from .models import X

import json


class MyClassBasedView(UnfoldModelAdminViewMixin, TemplateView):
    title = "Custom Title"  # required: custom page header title
    permission_required = ()  # required: tuple of permissions
    template_name = "admin_dashboards/dashboard_1.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "kpis": [
                    {
                        "title": "Total Active Users (Last 7 days)",
                        "metric": 10,
                    },
                    {
                        "title": "Number of Polls (Last 7 days)",
                        "metric": 7,
                    },
                    {
                        "title": "Total Active Organisations",
                        "metric": 18,
                    },
                ],
                "dauChartData": json.dumps(
                    {
                        "datasets": [
                            {
                                "data": [0, 1, 3, 2, 5, 8, 7],
                                "borderColor": "rgb(147 51 234)",
                            }
                        ],
                        "labels": [
                            "2024-11-18",
                            "2024-11-19",
                            "2024-11-20",
                            "2024-11-21",
                            "2024-11-22",
                            "2024-11-23",
                            "2024-11-24",
                        ],
                    }
                ),
                "dpsChartData": json.dumps(
                    {
                        "datasets": [
                            {
                                "data": [7, 15, 12, 23, 5, 10, 18],
                                "borderColor": "rgb(147 51 234)",
                            }
                        ],
                        "labels": [
                            "2024-11-18",
                            "2024-11-19",
                            "2024-11-20",
                            "2024-11-21",
                            "2024-11-22",
                            "2024-11-23",
                            "2024-11-24",
                        ],
                    }
                ),
                "table": {
                    "headers": ["Awesome column", "This one too!"],
                    "rows": [
                        ["a", "b"],
                        ["c", "d"],
                        ["e", "f"],
                    ],
                },
            }
        )

        return context


@admin.register(X)
class CustomAdmin(ModelAdmin):
    def get_urls(self):
        custom_view = self.admin_site.admin_view(
            MyClassBasedView.as_view(model_admin=self)
        )

        return super().get_urls() + [
            path("dashboard", custom_view, name="dashboard"),
        ]
