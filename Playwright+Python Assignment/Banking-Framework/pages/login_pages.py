from playwright.sync_api import Page

class LoginPage:

    def __init__(self, page: Page):
        self.page = page

        self.customer_login_btn = page.locator("//button[contains(text(),'Customer Login')]")
        self.manager_login_btn = page.locator("//button[contains(text(),'Bank Manager Login')]")
        self.customer_dropdown = page.locator("#userSelect")
        self.login_btn = page.locator("button:has-text('Login')")
        self.deposit_button = page.locator("button:has-text('Deposit')")

    def navigate(self):
        self.page.goto(
            "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
        )

    def click_customer_login(self):
        self.customer_login_btn.click()

    def click_manager_login(self):
        self.manager_login_btn.click()

    def select_customer(self, customer_name: str):
        self.customer_dropdown.select_option(label=customer_name)

    def click_login(self):
        self.login_btn.click()

    def login(self, customer_name: str):
        self.click_customer_login()
        self.select_customer(customer_name)
        self.click_login()
        self.deposit_button.wait_for()
