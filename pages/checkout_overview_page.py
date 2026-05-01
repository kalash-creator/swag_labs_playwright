from .base_page import BasePage
from utils.helpers import parse_price


class CheckoutOverviewPage(BasePage):
    ITEM_TOTAL = ".summary_subtotal_label"
    TAX = ".summary_tax_label"
    TOTAL = ".summary_total_label"
    FINISH = "[data-test='finish']"
    CANCEL = "[data-test='cancel']"

    def get_item_total(self) -> float:
        text = self.page.locator(self.ITEM_TOTAL).inner_text()
        return parse_price(text.split("$")[-1])

    def get_tax(self) -> float:
        text = self.page.locator(self.TAX).inner_text()
        return parse_price(text.split("$")[-1])

    def get_total(self) -> float:
        text = self.page.locator(self.TOTAL).inner_text()
        return parse_price(text.split("$")[-1])

    def click_finish(self):
        self.page.click(self.FINISH)

    def click_cancel(self):
        self.page.click(self.CANCEL)