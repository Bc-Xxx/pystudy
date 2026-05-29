import re
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://quotes.toscrape.com/")
    print(page.title())
    page.get_by_role("link", name="Login").click()
    page.locator("#username").click()
    page.keyboard.type("admin", delay=100)
    page.locator("#password").click()
    page.keyboard.type("123", delay=100)

    page.locator("input[type='submit']").click()
    page.wait_for_load_state("networkidle")
    # page.get_by_role("textbox", name="Login").click()
    expect(page.get_by_role("link", name="Logout")).to_be_visible()
    print("登录成功，出现 Logout 链接，测试通过")

    browser.close()
