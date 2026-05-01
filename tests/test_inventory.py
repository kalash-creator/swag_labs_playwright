from pages.inventory_page import InventoryPage


class TestInventory:

    # TC_INV_01
    def test_product_count(self, logged_in_page):
        inventory = InventoryPage(logged_in_page)
        assert inventory.get_product_count() == 6

    # TC_INV_02
    def test_sort_price_low_to_high(self, logged_in_page):
        inventory = InventoryPage(logged_in_page)

        inventory.sort_by("lohi")
        prices = inventory.get_all_product_prices()
        prices = [float(p.replace("$", "")) for p in prices]

        assert prices == sorted(prices)

    # TC_INV_03
    def test_sort_name_z_to_a(self, logged_in_page):
        inventory = InventoryPage(logged_in_page)

        inventory.sort_by("za")
        names = inventory.get_all_product_names()

        assert names == sorted(names, reverse=True)

    # TC_INV_04
    def test_add_to_cart(self, logged_in_page):
        inventory = InventoryPage(logged_in_page)

        inventory.add_product_to_cart_by_name("Sauce Labs Backpack")
        inventory.add_product_to_cart_by_name("Sauce Labs Bike Light")

        assert inventory.get_cart_badge_count() == 2

    # TC_INV_05
    def test_remove_from_cart(self, logged_in_page):
        inventory = InventoryPage(logged_in_page)

        inventory.add_product_to_cart_by_name("Sauce Labs Backpack")
        inventory.remove_product_from_cart_by_name("Sauce Labs Backpack")

        assert inventory.get_cart_badge_count() == 0