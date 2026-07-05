import pytest
from playwright.sync_api import sync_playwright

def test_title():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.wait_for_timeout(3000)
        page.goto("https://playwright.dev/")
        assert "Playwright" in page.title()
        browser.close()
