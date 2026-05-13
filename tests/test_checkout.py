from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_info_page import CheckoutInfoPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_complete_page import CheckoutCompletePage


class TestCheckout:

    def _go_to_checkout(self, page) -> None:
        inventory = InventoryPage(page)
        inventory.add_product_to_cart_by_name("Sauce Labs Backpack")
        inventory.go_to_cart()

        cart = CartPage(page)
        cart.click_checkout()

        page.wait_for_url("**/checkout-step-one.html")

    # TC_CHK_01
    def test_missing_first_name(self, logged_in_page):
        self._go_to_checkout(logged_in_page)

        checkout = CheckoutInfoPage(logged_in_page)
        checkout.fill_info("", "Doe", "12345")
        checkout.click_continue()

        assert checkout.is_error_displayed()
        assert "First Name is required" in checkout.get_error_message()

    # TC_CHK_02
    def test_missing_last_name(self, logged_in_page):
        self._go_to_checkout(logged_in_page)

        checkout = CheckoutInfoPage(logged_in_page)
        checkout.fill_info("John", "", "12345")
        checkout.click_continue()

        assert checkout.is_error_displayed()
        assert "Last Name is required" in checkout.get_error_message()

    # TC_CHK_03
    def test_missing_zip(self, logged_in_page):
        self._go_to_checkout(logged_in_page)

        checkout = CheckoutInfoPage(logged_in_page)
        checkout.fill_info("John", "Doe", "")
        checkout.click_continue()

        assert checkout.is_error_displayed()
        assert "Postal Code is required" in checkout.get_error_message()

    # TC_CHK_04
    def test_valid_checkout(self, logged_in_page):
        self._go_to_checkout(logged_in_page)

        checkout = CheckoutInfoPage(logged_in_page)
        checkout.fill_info("John", "Doe", "12345")
        checkout.click_continue()

        logged_in_page.wait_for_url("**/checkout-step-two.html")

        assert "checkout-step-two.html" in logged_in_page.url

    # TC_CHK_05
    def test_complete_order(self, logged_in_page):
        self._go_to_checkout(logged_in_page)

        checkout = CheckoutInfoPage(logged_in_page)
        checkout.fill_info("John", "Doe", "12345")
        checkout.click_continue()

        logged_in_page.wait_for_url("**/checkout-step-two.html")

        overview = CheckoutOverviewPage(logged_in_page)
        overview.click_finish()

        logged_in_page.wait_for_url("**/checkout-complete.html")

        complete = CheckoutCompletePage(logged_in_page)
        inventory = InventoryPage(logged_in_page)

        assert complete.get_complete_header() == "Thank you for your order!"
        assert inventory.get_cart_badge_count() == 0

    # TC_E2E_01
    def test_full_flow(self, logged_in_page):
        inventory = InventoryPage(logged_in_page)

        inventory.add_product_to_cart_by_name("Sauce Labs Backpack")
        assert inventory.get_cart_badge_count() == 1

        inventory.go_to_cart()

        cart = CartPage(logged_in_page)
        assert cart.get_item_count() == 1
        assert "Sauce Labs Backpack" in cart.get_item_names()

        cart.click_checkout()

        checkout = CheckoutInfoPage(logged_in_page)
        checkout.fill_info("John", "Doe", "12345")
        checkout.click_continue()

        logged_in_page.wait_for_url("**/checkout-step-two.html")

        overview = CheckoutOverviewPage(logged_in_page)
        overview.click_finish()

        logged_in_page.wait_for_url("**/checkout-complete.html")

        complete = CheckoutCompletePage(logged_in_page)

        assert complete.get_complete_header() == "Thank you for your order!"
        assert "checkout-complete.html" in logged_in_page.url