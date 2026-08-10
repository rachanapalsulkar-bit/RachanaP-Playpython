from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self):
        self.page.goto("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")

    def login(self, customer_name: str):
        # Select the Customer Login option and sign in as the given user
        self.page.click('button:has-text("Customer Login")')
        self.page.locator('select[ng-model="custId"]').select_option(label=customer_name)
        self.page.click('button:has-text("Login")')
        self.page.locator('button:has-text("Deposit")').wait_for()
       