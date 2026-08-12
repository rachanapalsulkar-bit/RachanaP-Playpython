class CustomerPage:

    def __init__(self, page):
        self.page = page

        self.customer_dropdown = page.locator("#userSelect")
        self.login_btn = page.locator("button:has-text('Login')")

    def select_customer(self, customer_name):
        self.customer_dropdown.select_option(label=customer_name)

    def click_login(self):
        self.login_btn.click()

    def login(self, customer_name):
        self.select_customer(customer_name)
        self.click_login()