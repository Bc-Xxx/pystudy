import pytest
import re
from playwright.sync_api import expect


class TestLoginPage:
    def test_login_page_title(self, login_page):
        expect(login_page).to_have_title("Quotes to Scrape")

    def test_login_form_exists(self, login_page):
        username_input = login_page.locator("#username")
        expect(username_input).to_be_visible()
        password_input = login_page.locator("#password")
        expect(password_input).to_be_visible()

    def test_login_button_exists(self, login_page):
        login_button = login_page.locator('input[type="submit"]')
        expect(login_button).to_be_visible()

    @pytest.mark.parametrize("username, password", [
        ("", ""),
        ("admin", "123"),
    ])
    def test_invalid_login(self, login_page, username, password):
        login_page.locator("#username").fill(username)
        login_page.locator("#password").fill(password)
        login_page.locator("input[type=submit]").click()
        expect(login_page).to_have_url(re.compile("/login"))
