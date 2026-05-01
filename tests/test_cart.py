from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


class TestCart:

    # TC_CART_01
    def test_cart_item(self, logged_in_page):
        inventory = InventoryPage(logged_in_page)
        inventory.add_product_to_cart_by_name("Sauce Labs Backpack")
        inventory.go_to_cart()

        cart = CartPage(logged_in_page)

        assert cart.get_item_count() == 1
        assert "Sauce Labs Backpack" in cart.get_item_names()

    # TC_CART_02
    def test_remove_item(self, logged_in_page):
        inventory = InventoryPage(logged_in_page)
        inventory.add_product_to_cart_by_name("Sauce Labs Backpack")
        inventory.go_to_cart()

        cart = CartPage(logged_in_page)
        cart.remove_item_by_name("Sauce Labs Backpack")

        assert cart.get_item_count() == 0