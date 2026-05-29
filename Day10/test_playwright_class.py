from playwright.sync_api import sync_playwright, expect


class TestQuotesPage:
    def test_page_title(self, quotes_page):
        expect(quotes_page).to_have_title("Quotes to Scrape")

    def test_page_has_quotes(self, quotes_page):
        quotes = quotes_page.locator('.quote')
        expect(quotes).to_have_count(10)

    def test_login_button_exists(self, quotes_page):
        login_link = quotes_page.get_by_role("link", name="Login")
        expect(login_link).to_be_visible()
