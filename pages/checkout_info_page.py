from .base_page import BasePage


class CheckoutInfoPage(BasePage):
    FIRST_NAME = "[data-test='firstName']"
    LAST_NAME = "[data-test='lastName']"
    POSTAL_CODE = "[data-test='postalCode']"
    CONTINUE = "[data-test='continue']"
    CANCEL = "[data-test='cancel']"
    ERROR = "[data-test='error']"

    def fill_info(self, first_name: str, last_name: str, postal_code: str):
        self.page.fill(self.FIRST_NAME, first_name)
        self.page.fill(self.LAST_NAME, last_name)
        self.page.fill(self.POSTAL_CODE, postal_code)

    def click_continue(self):
        self.page.click(self.CONTINUE)

    def click_cancel(self):
        self.page.click(self.CANCEL)

    def get_error_message(self) -> str:
        return self.page.locator(self.ERROR).inner_text()

    def is_error_displayed(self) -> bool:
        return self.page.locator(self.ERROR).is_visible()