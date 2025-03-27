import json


def dashboard_callback(request, context):
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
