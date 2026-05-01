from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_info_page import CheckoutInfoPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_complete_page import CheckoutCompletePage


class TestCheckout:

    def _go_to_checkout(self, page):
        inventory = InventoryPage(page)
        inventory.add_product_to_cart_by_name("Sauce Labs Backpack")
        inventory.go_to_cart()

        cart = CartPage(page)
        cart.click_checkout()

    # TC_CHK_01
    def test_missing_first_name(self, logged_in_page):
        self._go_to_checkout(logged_in_page)

        checkout = CheckoutInfoPage(logged_in_page)
        checkout.fill_info("", "Doe", "12345")
        checkout.click_continue()

        assert checkout.is_error_displayed()

    # TC_CHK_02
    def test_missing_last_name(self, logged_in_page):
        self._go_to_checkout(logged_in_page)

        checkout = CheckoutInfoPage(logged_in_page)
        checkout.fill_info("John", "", "12345")
        checkout.click_continue()

        assert checkout.is_error_displayed()

    # TC_CHK_03
    def test_missing_zip(self, logged_in_page):
        self._go_to_checkout(logged_in_page)

        checkout = CheckoutInfoPage(logged_in_page)
        checkout.fill_info("John", "Doe", "")
        checkout.click_continue()

        assert checkout.is_error_displayed()

    # TC_CHK_04
    def test_valid_checkout(self, logged_in_page):
        self._go_to_checkout(logged_in_page)

        checkout = CheckoutInfoPage(logged_in_page)
        checkout.fill_info("John", "Doe", "12345")
        checkout.click_continue()

        assert "checkout-step-two" in logged_in_page.url

    # TC_CHK_05
    def test_complete_order(self, logged_in_page):
        self._go_to_checkout(logged_in_page)

        checkout = CheckoutInfoPage(logged_in_page)
        checkout.fill_info("John", "Doe", "12345")
        checkout.click_continue()

        overview = CheckoutOverviewPage(logged_in_page)
        overview.click_finish()

        complete = CheckoutCompletePage(logged_in_page)

        assert "Thank you for your order!" in complete.get_complete_header()

    # TC_E2E_01
    def test_full_flow(self, logged_in_page):
        inventory = InventoryPage(logged_in_page)
        inventory.add_product_to_cart_by_name("Sauce Labs Backpack")
        inventory.go_to_cart()

        cart = CartPage(logged_in_page)
        cart.click_checkout()

        checkout = CheckoutInfoPage(logged_in_page)
        checkout.fill_info("John", "Doe", "12345")
        checkout.click_continue()

        overview = CheckoutOverviewPage(logged_in_page)
        overview.click_finish()

        complete = CheckoutCompletePage(logged_in_page)

        assert "Thank you for your order!" in complete.get_complete_header()