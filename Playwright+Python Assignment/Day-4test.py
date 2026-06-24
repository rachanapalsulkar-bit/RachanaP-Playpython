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


   #####################################################
   #Perform login, validate success & error scenarios
   #####################################################
   
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    print("Current URL:", page.url)
    page.wait_for_timeout(10000)  # Wait for 3 seconds
    browser.close()