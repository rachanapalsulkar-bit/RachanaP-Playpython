from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator('input[name="username"]')
        self.password_input = page.locator('input[name="password"]')
        self.login_button = page.locator('button[type="submit"]')
        self.dashboard_header = page.locator('h6.oxd-topbar-header-breadcrumb-module')
        self.invalid_login_error = page.locator('.oxd-text.oxd-text--p.oxd-alert-content-text')

    def goto(self):
        self.page.goto(
            "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login",
            wait_until="domcontentloaded",
        )

    def login(self, username: str, password: str):
        self.username_input.wait_for()
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def assert_login_success(self):
        expect(self.dashboard_header).to_have_text("Dashboard")

    def assert_login_failed(self, message: str = "Invalid credentials"):
        # use contains to avoid exact text mismatch from extra whitespace
        expect(self.invalid_login_error).to_contain_text(message)
