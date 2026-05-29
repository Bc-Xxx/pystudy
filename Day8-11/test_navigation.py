import re
from playwright.sync_api import expect


class TestNavigation:
    def test_click_next_page(self, quotes_page):
        quotes_page.get_by_role("link", name="Next").click()
        quotes_page.wait_for_load_state("networkidle")
        expect(quotes_page.locator('.quote')).to_have_count(10)

    def test_url_contains_page_2(self, quotes_page):
        quotes_page.get_by_role("link", name="Next").click()
        quotes_page.wait_for_load_state("networkidle")
        expect(quotes_page).to_have_url(re.compile("/page/2"))

    def test_second_page_has_quotes(self, quotes_page):
        quotes_page.get_by_role("link", name="Next").click()
        quotes_page.wait_for_load_state("networkidle")
        quotes = quotes_page.locator('.quote')
        expect(quotes).to_have_count(10)
