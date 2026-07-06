# test_example.py
def test_saucedemo_title(browser):
    page = browser.new_page()
    page.goto("https://www.saucedemo.com")
    assert "Swag Labs" in page.title()
