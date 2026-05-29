# 参数化测试，用一个测试函数测试多组数据
import pytest
from playwright.sync_api import expect


@pytest.mark.parametrize("url,title", [
    ("https://quotes.toscrape.com/", "Quotes to Scrape"),
    ("https://quotes.toscrape.com/login", "Quotes to Scrape"),
])
def test_page_title(page, url, title):
    page.goto(url)
    expect(page).to_have_title(title)
