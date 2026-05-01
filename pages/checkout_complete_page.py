from .base_page import BasePage


class CheckoutCompletePage(BasePage):
    HEADER = ".complete-header"
    TEXT = ".complete-text"
    BACK_HOME = "[data-test='back-to-products']"

    def get_complete_header(self) -> str:
        return self.page.locator(self.HEADER).inner_text()

    def get_complete_text(self) -> str:
        return self.page.locator(self.TEXT).inner_text()

    def click_back_home(self):
        self.page.click(self.BACK_HOME)