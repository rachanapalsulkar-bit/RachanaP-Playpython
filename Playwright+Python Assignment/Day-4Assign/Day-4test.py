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

   #########################################################
  
def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://example.com")

        # Locator examples
        heading = page.locator("h1")              # by tag
        link = page.locator("text=More information")  # by text
        button = page.locator("#submit")          # by id
        input_box = page.locator("input[name='q']")  # by attribute

        print(heading.text_content())
        browser.close()

run()

###============Use assertions========####

with sync_playwright() as p:
    page = p.chromium.launch().new_page()

    page.goto("https://www.google.com")

    assert "Google" in page.title()
    assert page.locator("textarea[name='q']").is_visible()
    page.wait_for_timeout(1000)
    print("Assertions Passed")


#######UI interaction-->Sort products, add items, validate cart#########

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    # Add item to cart
    page.click("#add-to-cart-sauce-labs-backpack")

    # Assertions
    assert page.title() == "Swag Labs"
    assert page.locator(".shopping_cart_badge").text_content() == "1"

    print("Item added successfully")

    page.wait_for_timeout(3000)
    browser.close()

    ##################Complete workflow-->Checkout flow, validate confirmation########
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
     browser = p.chromium.launch(headless=False)
     page = browser.new_page()

    # Login
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
     # Add item
    page.click("#add-to-cart-sauce-labs-backpack")
    page.click(".shopping_cart_link")

    # Checkout
    page.click("#checkout")

    # Fill details
    page.fill("#first-name", "John")
    page.fill("#last-name", "Doe")
    page.fill("#postal-code", "12345")

    page.click("#continue")
    page.click("#finish")

    # Check success message
    assert "Thank you" in page.locator(".complete-header").text_content()
    print("Order Placed Successfully!")

    page.wait_for_timeout(3000)
    browser.close()


    #########=====Complete workflow	Checkout flow, validate confirmation=====#########

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    page = p.chromium.launch().new_page()

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Launch the browser
    browser = p.chromium.launch(headless=False)

    # Create a new browser context (like a fresh profile)
    context = browser.new_context()

    # Open a new page (tab)
    page = context.new_page()

    # Navigate to a site
    page.goto("https://example.com")

    print("✅ Page loaded successfully!")

    # Close everything
    browser.close()
