# pages/dashboard_page.py
from playwright.sync_api import Page, expect

class DashboardPage:
    def __init__(self, page: Page):
        self.page = page
        # Stable locator for header
        self.dashboard_header = page.get_by_role("heading", name="Dashboard")
        # Consistent locator name for Employee Distribution widget
        self.employee_distribution_by_location_locator = page.get_by_text(
            "Employee Distribution by Location",
            exact=True,
        )

    def assert_dashboard_loaded(self):
        expect(self.dashboard_header).to_have_text("Dashboard", timeout=15 * 1000)
        expect(self.employee_distribution_by_location_locator).to_be_visible(timeout=15 * 1000)

    def screenshot_employee_distribution(self, path: str):
        self.employee_distribution_by_location_locator.screenshot(path=path)
