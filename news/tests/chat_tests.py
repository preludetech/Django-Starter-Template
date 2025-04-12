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


def expect_online_count(page, count):
    expect(page.locator("#users-online-count")).to_have_text(f"Users online: {count}")


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

    url = reverse_url(live_server, "article", args=[article.id])

    page1.goto(url)

    expect_online_count(page1, 1)
    page2.goto(url)
    expect_online_count(page1, 2)
    expect_online_count(page2, 2)

    message_from_1 = "This is a message from one to two"
    message_from_2 = "This is a message from two to one"

    page1.get_by_role("textbox", name="Message*").click()
    page1.get_by_role("textbox", name="Message*").fill(message_from_1)
    page1.get_by_role("button", name="Submit").click()

    page1.get_by_text(message_from_1)
    page2.get_by_text(message_from_1)

    page2.get_by_role("textbox", name="Message*").click()
    page2.get_by_role("textbox", name="Message*").fill(message_from_2)
    page2.get_by_role("button", name="Submit").click()

    page1.get_by_text(message_from_2)
    page2.get_by_text(message_from_2)
