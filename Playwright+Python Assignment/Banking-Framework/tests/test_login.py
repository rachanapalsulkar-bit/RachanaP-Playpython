from typing import Any

from playwright.sync_api import expect
from pages import LoginPage

def test_valid_login(page: Any):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("Harry Potter")
    
    # Wait for navigation to account page
    page.wait_for_url("**/#/account", timeout=30000)
    
    # Assert Deposit button is visible
    login_page.assert_login_success()

def test_transaction(page: Any):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("Harry Potter")
    
    # Wait for navigation to account page
    page.wait_for_url("**/#/account", timeout=300000000)
    
    # Perform a transaction
    login_page.Transaction()
    