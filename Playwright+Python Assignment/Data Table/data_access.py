from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # Set to True for headless mode
    page = browser.new_page()
    
    # 1. Navigate to your target website
    page.goto("https://the-internet.herokuapp.com/tables")
    
    # 2. Locate data associated with "Smith"

    smith_row = page.locator("tr", has_text="Smith") 
    
    # Example B: If you want to extract text from that specific element
    user_data = smith_row.inner_text()
    print(f"Data for Smith: {user_data}")
    
    browser.close()