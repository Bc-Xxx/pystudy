import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.douban.com/")
    page.get_by_role("textbox", name="书籍、电影、音乐、小组、小站、成员").click()
    page.get_by_role("textbox", name="书籍、电影、音乐、小组、小站、成员").fill("曾沛慈")
    page.get_by_role("button", name="搜索").click()
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="曾沛慈").click()
    page1 = page1_info.value

    # ---------------------

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
