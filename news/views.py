from django.shortcuts import render, get_object_or_404
from . import models


def index(request):
    articles = models.Article.objects.all()
    context = {"articles": articles}
    return render(request, "news/index.html", context=context)


def article(request, article_id):
    article = get_object_or_404(models.Article, pk=article_id)
    context = {"article": article, "content": article.rendered_content(request)}
    return render(request, "news/article.html", context=context)
