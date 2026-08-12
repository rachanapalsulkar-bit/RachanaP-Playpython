from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        # Locators
        self.add_to_cart_button = "[data-test='add-to-cart-sauce-labs-backpack']"
        self.cart_link = "[data-test='shopping-cart-link']"
        self.inventory_container = ".inventory_container"

    def is_loaded(self):
        """Check if inventory page is loaded"""
        return self.page.locator(self.inventory_container).is_visible()

    def add_item(self):
        """Add first item to cart"""
        self.page.click(self.add_to_cart_button)

    def go_to_cart(self):
        """Navigate to shopping cart"""
        self.page.click(self.cart_link)
