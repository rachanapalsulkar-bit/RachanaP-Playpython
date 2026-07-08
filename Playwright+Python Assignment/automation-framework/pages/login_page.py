from playwright.sync_api import page

class LoginPage:
    def __init__(self, page: page):
        self.page = page
        # Locators
        self.username_input = "#user-name"
        self.password_input = "#password"
        self.login_button = "#login-button"

    def goto(self):
        """Navigate to the login page"""
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username: str, password: str):
        """Perform login action"""
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)
