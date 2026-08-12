from pages.login_page import LoginPage
from playwright.sync_api import Page

def test_valid_login(page: Page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")
    assert page.url.endswith("/inventory.html")
