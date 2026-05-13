from .base_page import BasePage


class ProductDetailPage(BasePage):
    NAME = ".inventory_details_name"
    DESCRIPTION = ".inventory_details_desc"
    PRICE = ".inventory_details_price"
    ADD_TO_CART = "button:has-text('Add to cart')"
    BACK_BUTTON = "[data-test='back-to-products']"

    def get_product_name(self) -> str:
        return self.page.locator(self.NAME).inner_text()

    def get_product_description(self) -> str:
        return self.page.locator(self.DESCRIPTION).inner_text()

    def get_product_price(self) -> str:
        return self.page.locator(self.PRICE).inner_text()

    def click_add_to_cart(self):
        self.page.click(self.ADD_TO_CART)

    def click_back_to_products(self):
        self.page.click(self.BACK_BUTTON)

    def is_add_to_cart_visible(self) -> bool:
        return self.page.locator(self.ADD_TO_CART).is_visible()

    def is_back_to_products_visible(self) -> bool:
        return self.page.locator(self.BACK_BUTTON).is_visible()