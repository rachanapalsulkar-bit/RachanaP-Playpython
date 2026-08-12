class LoginPage:

    def __init__(self, page):
        self.page = page

        self.customer_login_btn = page.locator(
            "//button[contains(text(),'Customer Login')]"
        )

        self.manager_login_btn = page.locator(
            "//button[contains(text(),'Bank Manager Login')]"
        )

    def navigate(self):
        self.page.goto(
            "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
        )

    def click_customer_login(self):
        self.customer_login_btn.click()

    def click_manager_login(self):
        self.manager_login_btn.click()