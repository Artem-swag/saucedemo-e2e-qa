import pytest
from playwright.sync_api import Page

from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


PRODUCT = "Sauce Labs Backpack"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"


class TestPurchaseE2E:
    """Основной сценарий: вход → добавление товара → корзина → оформление → успех."""

    def test_full_purchase_flow(self, login_page):
        # 1. Вход
        login_page.login(USERNAME, PASSWORD)
        inventory = InventoryPage(login_page.page)

        # 2. Добавление товара
        inventory.add_product_to_cart(PRODUCT)
        inventory.expect_cart_count("1")

        # 3. Корзина
        inventory.go_to_cart()
        cart = CartPage(login_page.page)
        cart.expect_product_in_cart(PRODUCT)
        cart.proceed_to_checkout()

        # 4. Оформление
        checkout = CheckoutPage(login_page.page)
        checkout.fill_info("Test", "User", "123456")
        checkout.finish_order()

        # 5. Проверка успеха
        checkout.expect_success()


class TestNegativeCases:
    """Негативные сценарии: проверка обработки ошибочных входных данных."""

    def test_login_with_invalid_password(self, login_page):
        login_page.login(USERNAME, "wrong_password")
        login_page.expect_error(
            "Epic sadface: Username and password do not match any user in this service"
        )
        # проверяем, что остались на странице входа
        assert "inventory" not in login_page.page.url

    def test_checkout_with_empty_fields(self, login_page):
        login_page.login(USERNAME, PASSWORD)
        inventory = InventoryPage(login_page.page)
        inventory.add_product_to_cart(PRODUCT)
        inventory.go_to_cart()

        cart = CartPage(login_page.page)
        cart.proceed_to_checkout()

        checkout = CheckoutPage(login_page.page)
        checkout.click_continue_without_info()
        checkout.expect_error("Error: First Name is required")
