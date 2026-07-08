# tests/saucedemo/test_inventory.py
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_add_item(page):
    LoginPage(page).goto()
    LoginPage(page).login("standard_user", "secret_sauce")
    inv = InventoryPage(page)
    assert inv.is_loaded()
    inv.add_item()
    inv.go_to_cart()
    assert page.url.endswith("/cart.html")
