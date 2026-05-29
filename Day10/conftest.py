import pytest
from playwright.sync_api import sync_playwright, expect


@pytest.fixture
def quotes_page(page):
    page.goto("https://quotes.toscrape.com/")
    return page


@pytest.fixture
def login_page(page):
    page.goto("https://quotes.toscrape.com/login")
    return page



