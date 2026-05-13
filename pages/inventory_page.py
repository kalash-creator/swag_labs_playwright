from .base_page import BasePage


class InventoryPage(BasePage):
    TITLE = ".title"
    INVENTORY_ITEMS = ".inventory_item"
    PRODUCT_NAMES = ".inventory_item_name"
    PRODUCT_PRICES = ".inventory_item_price"
    SORT_DROPDOWN = "[data-test='product-sort-container']"
    CART_BADGE = ".shopping_cart_badge"
    CART_ICON = ".shopping_cart_link"
    MENU_BUTTON = "#react-burger-menu-btn"
    LOGOUT_LINK = "#logout_sidebar_link"

    def get_product_count(self) -> int:
        return self.page.locator(self.INVENTORY_ITEMS).count()

    def get_all_product_names(self):
        return self.page.locator(self.PRODUCT_NAMES).all_inner_texts()

    def get_all_product_prices(self):
        return self.page.locator(self.PRODUCT_PRICES).all_inner_texts()

    def sort_by(self, value: str):
        self.page.select_option(self.SORT_DROPDOWN, value)

    def add_product_to_cart_by_name(self, name: str):
        item = self.page.locator(self.INVENTORY_ITEMS).filter(has_text=name)
        item.get_by_role("button", name="Add to cart").click()

    def remove_product_from_cart_by_name(self, name: str):
        item = self.page.locator(self.INVENTORY_ITEMS).filter(has_text=name)
        item.get_by_role("button", name="Remove").click()

    def get_cart_badge_count(self) -> int:
        badge = self.page.locator(self.CART_BADGE)
        if badge.is_visible():
            return int(badge.inner_text())
        return 0

    def go_to_cart(self):
        self.page.click(self.CART_ICON)

    def click_product_name(self, name: str):
        self.page.locator(self.PRODUCT_NAMES, has_text=name).click()

    def logout(self):
        self.page.click(self.MENU_BUTTON)
        self.page.click(self.LOGOUT_LINK)