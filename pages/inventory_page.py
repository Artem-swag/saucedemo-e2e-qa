from playwright.sync_api import Page, expect


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_link = page.locator("#shopping_cart_container a")
        self.cart_badge = page.locator(".shopping_cart_badge")

    def add_product_to_cart(self, product_name: str):
        """Добавляет указанный товар в корзину по названию."""
        product = self.page.locator(".inventory_item").filter(
            has_text=product_name
        )
        product.get_by_role("button", name="Add to cart").click()

    def expect_cart_count(self, count: str):
        expect(self.cart_badge).to_have_text(count)

    def go_to_cart(self):
        self.cart_link.click()
