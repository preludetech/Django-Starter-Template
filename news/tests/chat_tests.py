from playwright.sync_api import Page, expect
from django.urls import reverse
from news.models import Article
import pytest
from datetime import date
from django.contrib.auth import get_user_model
from allauth.account.models import EmailAddress

User = get_user_model()


def reverse_url(
    live_server, viewname, urlconf=None, args=None, kwargs=None, current_app=None
):
    end = reverse(viewname, urlconf, args, kwargs, current_app)
    return f"{live_server.url}{end}"


def create_user(name):
    email = f"{name}@email.com"
    new_user = User.objects.create_user(
        email=email,
        password=email,
    )
    new_user.save()
    new_user.is_active = True
    new_user.save()

    new_email_address = EmailAddress(
        user_id=new_user.id,
        email=email,
        verified=True,
        primary=True,
    )
    new_email_address.save()
    return new_user


def log_user_in(live_server, page, user):
    url = reverse_url(live_server, "account_login")
    page.goto(url)
    page.get_by_role("textbox", name="Email*").fill(user.email)
    page.get_by_role("textbox", name="Password*").fill(user.email)
    page.get_by_role("button", name="Sign In").click()


@pytest.mark.django_db
def test_chat(channels_liver_server, browser):
    live_server = channels_liver_server

    article = Article.objects.create(date=date.today(), title="title", content="super")

    context1 = browser.new_context()
    context2 = browser.new_context()

    page1 = context1.new_page()
    page2 = context2.new_page()

    user1 = create_user("one")
    user2 = create_user("two")

    log_user_in(live_server, page1, user1)
    log_user_in(live_server, page2, user2)

    breakpoint()
    url = reverse_url(live_server, "article", args=[article.id])
