import os

from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_valid_login(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("Admin", "admin123")

    # Wait for dashboard URL after successful login
    page.wait_for_url("**/dashboard/**", timeout=30000)

    dashboard_page = DashboardPage(page)

    expect(dashboard_page.dashboard_header).to_have_text("Dashboard", timeout=15000)
    expect(dashboard_page.employee_distribution_by_location_locator).to_be_visible(timeout=15000)

    dashboard_page.employee_distribution_by_location_locator.scroll_into_view_if_needed()

    screenshot_dir = r"D:\Screenshot"
    os.makedirs(screenshot_dir, exist_ok=True)
    screenshot_path = os.path.join(screenshot_dir, "OrangeHRM_Dashboard.png")
    dashboard_page.screenshot_employee_distribution(screenshot_path)
