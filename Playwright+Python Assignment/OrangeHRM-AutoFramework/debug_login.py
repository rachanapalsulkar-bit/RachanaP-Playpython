from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login', wait_until='domcontentloaded')
    print('initial url', page.url)
    print('readyState', page.evaluate('document.readyState'))
    page.locator('input[name="username"]').fill('wronguser')
    page.locator('input[name="password"]').fill('wrongpass')
    page.locator('button[type="submit"]').click()
    page.wait_for_timeout(8000)
    print('after submit url', page.url)
    try:
        content = page.inner_text('body')
    except Exception as e:
        content = f'BODY ERROR: {e}'
    print('body text length', len(content))
    print('body snippet:', repr(content[:500]))
    loc = page.locator('text=Invalid credentials')
    print('invalid text locator count', loc.count())
    print('invalid text all', loc.all_text_contents())
    exact = page.locator('div[class*="oxd-alert-content"]')
    print('alert container count', exact.count())
    print('alert container texts', exact.all_text_contents())
    print('page html snippet:', page.content()[:1200])
    browser.close()
