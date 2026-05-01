from pages.login_page import LoginPage
from test_data.users import VALID_USER, INVALID_USER, LOCKED_OUT_USER


class TestLogin:

    # TC_LOGIN_01
    def test_successful_login(self, page):
        login = LoginPage(page)
        login.open()
        login.login(VALID_USER["username"], VALID_USER["password"])

        page.wait_for_url("**/inventory.html")
        assert "inventory.html" in page.url

    # TC_LOGIN_02
    def test_invalid_login(self, page):
        login = LoginPage(page)
        login.open()
        login.login(INVALID_USER["username"], INVALID_USER["password"])

        assert login.is_error_displayed()
        assert "do not match" in login.get_error_message()

    # TC_LOGIN_03
    def test_empty_username(self, page):
        login = LoginPage(page)
        login.open()
        login.login("", VALID_USER["password"])

        assert login.is_error_displayed()
        assert "Username is required" in login.get_error_message()

    # TC_LOGIN_04
    def test_empty_password(self, page):
        login = LoginPage(page)
        login.open()
        login.login(VALID_USER["username"], "")

        assert login.is_error_displayed()
        assert "Password is required" in login.get_error_message()

    # TC_LOGIN_05
    def test_locked_user(self, page):
        login = LoginPage(page)
        login.open()
        login.login(LOCKED_OUT_USER["username"], LOCKED_OUT_USER["password"])

        assert login.is_error_displayed()
        assert "locked out" in login.get_error_message()

    # TC_LOGIN_06
    def test_logout(self, logged_in_page):
        from pages.inventory_page import InventoryPage

        inventory = InventoryPage(logged_in_page)
        inventory.logout()

        assert "saucedemo.com" in logged_in_page.url