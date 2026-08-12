from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # headless=True for background run
    page = browser.new_page()
    
    # Navigate to the site
    page.goto("https://the-internet.herokuapp.com/tables")
    page.wait_for_selector("#table1", timeout=10000)

    # Locate Smith's row (first match)
    smith_row = page.locator("tr", has_text="Smith").first

    # Extract text
    user_data = smith_row.inner_text()
    print(f"Data for Smith: {user_data}")

    # Example: extract just the email cell
    email = smith_row.locator("td:nth-child(3)").inner_text()
    print(f"Smith's email: {email}")

    browser.close()
