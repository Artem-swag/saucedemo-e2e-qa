from playwright.sync_api import Page, expect


class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_name = page.get_by_placeholder("First Name")
        self.last_name = page.get_by_placeholder("Last Name")
        self.postal_code = page.get_by_placeholder("Zip/Postal Code")
        self.continue_button = page.get_by_role("button", name="Continue")
        self.finish_button = page.get_by_role("button", name="Finish")
        self.error_message = page.locator("[data-test='error']")
        self.complete_header = page.locator(".complete-header")

    def fill_info(self, first: str, last: str, zip_code: str):
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.postal_code.fill(zip_code)
        self.continue_button.click()

    def click_continue_without_info(self):
        self.continue_button.click()

    def expect_error(self, text: str):
        expect(self.error_message).to_be_visible()
        expect(self.error_message).to_contain_text(text)

    def finish_order(self):
        self.finish_button.click()

    def expect_success(self):
        expect(self.complete_header).to_have_text("Thank you for your order!")
