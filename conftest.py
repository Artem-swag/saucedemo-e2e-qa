import pytest
from playwright.sync_api import Page


@pytest.fixture(scope="function")
def login_page(page: Page):
    """Открывает SauceDemo и возвращает объект страницы входа."""
    page.goto("https://www.saucedemo.com/")
    from pages.login_page import LoginPage
    return LoginPage(page)
