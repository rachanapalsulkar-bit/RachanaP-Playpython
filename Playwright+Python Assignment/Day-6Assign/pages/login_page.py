class LoginPage:

    def __init__(self, page):
        self.page = page
        self.user = "#user-name"
        self.pwd = "#password"
        self.login_btn = "#login-button"

    def open(self):
        self.page.goto("https://www.saucedemo.com")

    def login(self, username, password):
        self.page.fill(self.user, username)
        self.page.fill(self.pwd, password)
        self.page.click(self.login_btn)