import pytest


@pytest.fixture
def quotes_page(page):
    page.goto('http://quotes.toscrape.com/')
    return page


@pytest.fixture
def login_page(page):
    page.goto('http://quotes.toscrape.com/login')
    return page
