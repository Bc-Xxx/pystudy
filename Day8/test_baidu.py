# from playwright.sync_api import sync_playwright
#
# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False, slow_mo=800)
#     page = browser.new_page()
#
#     # 推荐练习网站（稳定）
#     page.goto("https://www.saucedemo.com/")
#     print("标题:", page.title())
#
#     # 使用 get_by_xxx 定位
#     page.get_by_placeholder("Username").fill("standard_user")
#     page.get_by_placeholder("Password").fill("secret_sauce")
#     # page.get_by_role("button",name="user-name").fill("standard_user")
#     # page.fill("Username","standard_user")
#
#     page.get_by_role("button", name="Login").click()
#
#     # 断言是否登录成功
#     page.wait_for_url("**/inventory.html", timeout=5000)
#     print("✅ 登录成功！")
#
#     page.screenshot(path="login_success.png")
#     browser.close()

