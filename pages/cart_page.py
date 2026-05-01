from .base_page import BasePage


class CartPage(BasePage):
    CART_ITEMS = ".cart_item"
    ITEM_NAMES = ".inventory_item_name"
    CHECKOUT_BUTTON = "[data-test='checkout']"
    CONTINUE_SHOPPING = "[data-test='continue-shopping']"

    def get_item_count(self) -> int:
        return self.page.locator(self.CART_ITEMS).count()

    def get_item_names(self):
        return self.page.locator(self.ITEM_NAMES).all_inner_texts()

    def remove_item_by_name(self, name: str):
        item = self.page.locator(self.CART_ITEMS).filter(has_text=name)
        item.get_by_role("button", name="Remove").click()

    def click_checkout(self):
        self.page.click(self.CHECKOUT_BUTTON)

    def click_continue_shopping(self):
        self.page.click(self.CONTINUE_SHOPPING)