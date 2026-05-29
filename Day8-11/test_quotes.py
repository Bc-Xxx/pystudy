import pytest
from playwright.sync_api import expect


class TestQuotesPage:
    def test_page_title(self, quotes_page):
        expect(quotes_page).to_have_title("Quotes to Scrape")

    # 测试页面标题

    def test_quotes_count(self, quotes_page):
        quotes = quotes_page.locator('.quote')
        expect(quotes).to_have_count(10)

    # 测试名言数量是否为 10

    def test_all_quotes_have_author(self, quotes_page):
        quotes_page.wait_for_load_state("networkidle")
        author = quotes_page.locator('.author')
        expect(author).to_have_count(10)

    # 测试每条名言都有作者

    def test_next_button_exists(self, quotes_page):
        buttons=quotes_page.get_by_role("link",name="Next")
        expect(buttons).to_have_count(1)


    # 测试下一页按钮存在

    @pytest.mark.parametrize("keyword", ["life", "love", "world"])
    def test_quotes_contain_keyword(self, quotes_page, keyword):
        contains = quotes_page.locator(f'.text:has-text("{keyword}")').first
        expect(contains).to_be_visible()

# 测试名言包含特定关键词
