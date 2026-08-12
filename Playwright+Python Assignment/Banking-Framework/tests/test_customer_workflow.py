from pathlib import Path

from pages import LoginPage, CustomerPage, AccountPage


def test_customer_transaction_workflow(page):

    login = LoginPage(page)
    customer = CustomerPage(page)
    account = AccountPage(page)

    login.navigate()

    login.click_customer_login()

    customer.login("Harry Potter")

    # Deposit
    account.deposit(1000)

    balance_after_deposit = account.get_balance()
    print("Balance:", balance_after_deposit)

    # Withdraw
    account.withdraw(500)

    balance_after_withdraw = account.get_balance()
    print("Balance:", balance_after_withdraw)

    # Transactions
    account.open_transactions()

    assert page.locator("table").is_visible()
    page.locator("table").wait_for(state="visible")

    # Take a screenshot of the transactions page
    screenshot_dir = Path(r"C:\\Users\\rachana.palsulkar\\Rach-Play-Python")
    screenshot_path = screenshot_dir / "transactions.png"

    # Logout
    account.logout()
    page.wait_for_url("**/#/customer", timeout=500000)
    assert page.locator("#userSelect").is_visible()


