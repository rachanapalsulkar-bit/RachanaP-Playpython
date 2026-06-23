def test_saucedemo_title(page):
    page.goto("https://www.saucedemo.com/")
    assert "Swag Labs" in page.title()
    page.wait_for_timeout(100000)  # Wait for 3 seconds

####Command to execute the test: "pytest -v --headed --browser=chromium"


####Use Locator to get the placeholder for username and password fields
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    page = p.chromium.launch().new_page()

    page.goto("https://www.saucedemo.com/")

    print(page.locator("#user-name").get_attribute("placeholder"))
    print(page.locator("#password").get_attribute("placeholder"))

    page.context.browser.close()