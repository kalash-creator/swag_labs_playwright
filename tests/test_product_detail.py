from pages.inventory_page import InventoryPage
from pages.product_detail_page import ProductDetailPage


class TestProductDetail:

    # TC_PDP_01
    def test_product_details(self, logged_in_page):
        inventory = InventoryPage(logged_in_page)

        inventory.click_product_name("Sauce Labs Backpack")

        pdp = ProductDetailPage(logged_in_page)

        assert pdp.get_product_name() == "Sauce Labs Backpack"
        assert pdp.get_product_price() == "$29.99"
        assert len(pdp.get_product_description()) > 0
        assert pdp.is_add_to_cart_visible()
        assert pdp.is_back_to_products_visible()