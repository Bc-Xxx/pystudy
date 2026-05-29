from playwright.sync_api import sync_playwright

with sync_playwright() as p:
      browser = p.chromium.launch(headless=False)  # 打开浏览器窗口，方便看
      page = browser.new_page()
      page.goto("https://quotes.toscrape.com/")

      # 点击登录
      # page.get_by_role("link", name="login").click()
      # # page.screenshot(path="screenshot.png")
      # page.fill("#username", "test")
      # page.fill("#password", "123456")
      # page.click("input[type='submit']")
      # print("登录成功")

      # page.wait_for_load_state("networkidle")
      links=page.locator(".text").all_text_contents()
      for link in links:
            print(link)
      print("第一页名言打印完毕")
      page.get_by_role("link",name="Next").click()
      page.wait_for_load_state("networkidle")
      links2 = page.locator(".text").all_text_contents()
      for link in links2:
            print(link)
      print("第二页名言打印完毕")








      browser.close()


