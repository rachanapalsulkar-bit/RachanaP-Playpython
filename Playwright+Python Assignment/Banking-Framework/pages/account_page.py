class AccountPage:

    def __init__(self, page):
        self.page = page

        
        self.deposit_tab = page.locator("button[ng-click='deposit()']")
        self.withdraw_tab = page.locator("button[ng-click='withdrawl()']")
        self.transactions_tab = page.locator("button[ng-click='transactions()']")
        self.amount_textbox = page.locator("input[ng-model='amount']")
        self.submit_btn = page.locator("button[type='submit']")

        self.logout_btn = page.locator("button:has-text('Logout')")

        self.balance = page.locator(
            "//div[@class='center']/strong[2]"
        )

    def deposit(self, amount):
        self.deposit_tab.click()
        self.page.wait_for_selector("input[ng-model='amount']", timeout=500000)
        self.amount_textbox.fill(str(amount))
        self.submit_btn.click()

    def withdraw(self, amount):
        self.withdraw_tab.click()
        self.page.wait_for_selector("input[ng-model='amount']", timeout=5000)
        self.amount_textbox.fill(str(amount))
        self.submit_btn.click()

    def open_transactions(self):
        self.transactions_tab.click()
        self.page.wait_for_url("**/#/listTx", timeout=5000)
        self.page.wait_for_selector("table", state="visible", timeout=5000)

    def logout(self):
        self.logout_btn.wait_for(state="visible", timeout=5000)
        self.logout_btn.click()
        self.page.wait_for_url("**/#/customer", timeout=5000)
        self.page.locator("#userSelect").wait_for(state="visible", timeout=5000)

    def get_balance(self):
        return self.balance.text_content()