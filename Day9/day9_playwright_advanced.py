from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    # page.goto("https://quotes.toscrape.com/")
    # texts=page.locator(".text").all_text_contents()
    # for text in texts:
    #     print(text)
    # print("第一页打印完成")
    # page.get_by_role("link",name="Next").click()
    # page.wait_for_load_state("networkidle")
    # texts2 = page.locator(".text").all_text_contents()
    # for text in texts2:
    #       print(text)
    # print("第二页打印完成")
    # expect(page).to_have_title("Quotes to Scrape")
    # print("标题校验通过")
    # expect(page.locator(".text").first).to_be_visible()
    # print("第一个名言可见，校验通过")

    # page.goto("https://quotes.toscrape.com/login")
    # # page.get_by_role("textbox",name="Username").click()
    # page.locator("#username").click()
    # page.keyboard.type("admin",delay=100)
    #
    # # page.get_by_role("textbox", name="Password").click()
    # page.locator("#password").click()
    # page.keyboard.type("123456", delay=100)
    # page.locator("input[type='submit']").hover()  # 悬停在按钮上
    # page.locator("input[type='submit']").click()
    # print("键盘鼠标操作完成")

    page.goto("https://quotes.toscrape.com/")
    page.screenshot(path="screenshot.png", full_page=True)
    page.locator(".text").first.screenshot(path="day9first.png")
    page.set_viewport_size({"width": 375, "height": 812})
    page.screenshot(path="day9.png")
    print("截图完成")

    requests_log = []
    page.on("request", lambda req: requests_log.append(f"{req.method} {req.url}"))
    responses_log = []
    page.on("response", lambda res: responses_log.append(f"{res.status} {res.url}"))

    page.goto("https://quotes.toscrape.com/")
    page.wait_for_load_state("networkidle")

    print(f"共捕获 {len(requests_log)} 个请求")
    for r in requests_log[:3]:  # 只看前3个
        print(f"  请求: {r}")
    for r in responses_log[:3]:
        print(f"  响应: {r}")

    # 多标签页 - 手动新开一个页面
    page2 = browser.new_page()            # 创建第二个标签页
    page2.goto("https://httpbin.org/get")
    print("第二个标签页URL:", page2.url)
    page2.close()                          # 关闭第二个标签页

    # 回到第一个标签页确认还能用
    page.goto("https://quotes.toscrape.com/")
    print("第一个标签页标题:", page.title())
    print("多标签页处理完成")

    browser.close()
