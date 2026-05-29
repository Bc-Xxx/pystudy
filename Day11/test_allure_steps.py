import allure
from playwright.sync_api import expect


@allure.title("测试登录功能")
@allure.story("用户登录")
def test_login_with_steps(page):
    with allure.step("步骤1：打开登录页面"):
        page.goto("https://quotes.toscrape.com/login")

    with allure.step("步骤2：输入用户名"):
        page.locator("#username").fill("admin")

    with allure.step("步骤3：输入密码"):
        page.locator("#password").fill("123")

    with allure.step("步骤4：点击登录按钮"):
        page.locator("input[type='submit']").click()

    with allure.step("步骤5：检查是否登录成功"):
        expect(page.locator("text=Logout")).to_be_visible()

    screenshot=page.screenshot()
    allure.attach(screenshot,name="登录成功截图",attachment_type=allure.attachment_type.PNG)