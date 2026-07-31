from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_valid_login(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("Admin", "admin123")

    # Wait for dashboard URL (increase timeout if needed)
    page.wait_for_url("**/dashboard/index", timeout=30000)
    # Instantiate DashboardPage AFTER login
    dashboard_page = DashboardPage(page)

    # Assert header text
    expect(dashboard_page.dashboard_header).to_have_text("Dashboard")

    page.screenshot(path="D:\\Screenshot\\OrangeHRM_Dashboard.png", full_page=True)



    # Close context
    page.context.close()
