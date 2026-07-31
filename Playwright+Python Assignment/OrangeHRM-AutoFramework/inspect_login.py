from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login', wait_until='domcontentloaded')
    page.locator('input[name="username"]').fill('wronguser')
    page.locator('input[name="password"]').fill('wrongpass')
    page.locator('button[type="submit"]').click()
    page.wait_for_timeout(5000)
    print(page.locator('body').text_content())
    browser.close()
