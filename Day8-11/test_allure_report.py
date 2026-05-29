import allure
from playwright.sync_api import expect


@allure.title("测试登录完整流程")
@allure.story("用户登录")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_full_flow(page):
    with allure.step("步骤1：打开登录页面"):
        page.goto("https://quotes.toscrape.com/login")
        page.wait_for_load_state("networkidle")

    with allure.step("步骤2：输入用户名密码"):
        page.locator("#username").fill("admin")
        page.locator("#password").fill("123")

    with allure.step("步骤3：点击登录按钮"):
        page.locator("input[type='submit']").click()
        page.wait_for_load_state("networkidle")

    with allure.step("步骤4：检查登录成功"):
        expect(page.locator("text=Logout")).to_be_visible()

    with allure.step("步骤5：添加截图"):
        screenshot = page.screenshot()
        allure.attach(screenshot, name="登录成功截图", attachment_type=allure.attachment_type.PNG)
