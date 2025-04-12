from django.db import models
from markdown_utils import render_markdown


class Article(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=300)
    content = models.TextField()

    def __str__(self):
        return self.title

    def rendered_content(self, request):
        return render_markdown(self.content, request)
