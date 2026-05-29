import allure
from playwright.sync_api import expect


@allure.title("测试页面标题")
@allure.description("检查页面标题是否正确")
@allure.severity(allure.severity_level.NORMAL)
def test_page_title(page):
    page.goto("https://quotes.toscrape.com/")
    expect(page).to_have_title("Quotes to Scrape")


@allure.title("测试名言数量")
@allure.description("检查页面上名言数量是否为10")
@allure.severity(allure.severity_level.CRITICAL)
def test_page_has_quotes(page):
    page.goto("https://quotes.toscrape.com/")
    quotes = page.locator('.quote')
    expect(quotes).to_have_count(10)
