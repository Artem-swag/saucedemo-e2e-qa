from playwright.sync_api import Page, expect


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.checkout_button = page.get_by_role("button", name="Checkout")
        self.cart_items = page.locator(".cart_item")

    def expect_product_in_cart(self, product_name: str):
        expect(self.cart_items.filter(has_text=product_name)).to_be_visible()

    def proceed_to_checkout(self):
        self.checkout_button.click()
        
