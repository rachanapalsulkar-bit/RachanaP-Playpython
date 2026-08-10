import pytest
from playwright.sync_api import sync_playwright
from pages import LoginPage

@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as pw:
        yield pw

@pytest.fixture(scope="session")
def browser(playwright):
    browser = playwright.chromium.launch(headless=False)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

@pytest.fixture
def login_page(page):
    return LoginPage(page)
