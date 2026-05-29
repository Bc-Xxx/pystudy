from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    # page.goto("https://quotes.toscrape.com/")
    # page.wait_for_load_state("networkidle")  # 1. 等页面加载完
    # expect(page).to_have_title("Quotes to Scrape")  # 2. 检查页面标题是否为 "Quotes to Scrape"
    # page.wait_for_selector(".text")  # 3. 等待 .text 元素出现
    # print(page.locator(".text").all_text_contents())  # 4. 打印出所有名言

    # 登录页面练习
    # 2.    用键盘输入用户名和密码
    # 3.    用鼠标悬停在登录按钮上
    # 4.    点击登录
    # page.goto("https://quotes.toscrape.com/login")
    # page.locator("input[name='username']").click()
    # page.keyboard.type("admin",delay=100)
    # page.locator("input[name='password']").click()
    # page.keyboard.type("12345678",delay=100)
    # page.locator("input[type='submit']").hover()
    # page.locator("input[type='submit']").click()

    # 截图和网络拦截
    # 2.    截取整个页面（full_page = True）
    # 3.    截取第一条名言的截图
    # 4.    监听所有网络请求，打印前3个请求

    # 必须先设置监听器，再 goto
    requests_log = []
    page.on("request", lambda req: requests_log.append(f"{req.method} {req.url}"))
    responses_log = []
    page.on("response", lambda res: responses_log.append(f"{res.status} {res.url}"))

    page.goto("https://quotes.toscrape.com/")
    page.wait_for_load_state("networkidle")

    page.screenshot(path="screenshot.png", full_page=True)  # 截取整个页面
    page.locator(".quote").first.screenshot(path="quote.png")  # 截取第一条名言

    print(f"共捕获 {len(requests_log)} 个请求")
    for r in requests_log[:3]:
        print(r)
    for r in responses_log[:3]:
        print(r)



    browser.close()
