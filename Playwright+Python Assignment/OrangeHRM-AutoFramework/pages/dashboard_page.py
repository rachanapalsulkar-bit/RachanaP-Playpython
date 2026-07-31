# pages/dashboard_page.py
from playwright.sync_api import Page, expect

from conftest import page

class DashboardPage:
    def __init__(self, page: Page):
        self.page = page
        self.dashboard_header = page.get_by_role("heading", name="Dashboard")
        self.employee_distribution_by_location_locator = page.get_by_text("Employee Distribution by Location")


    # Example action: verify dashboard is loaded
    def assert_dashboard_loaded(self):
        expect(self.dashboard_header).to_have_text("Dashboard")
        expect(self.employee_distribution_by_location_locator).to_be_visible(timeout=2 * 60 * 1000)

        
