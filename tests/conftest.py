import pytest
from playwright.sync_api import sync_playwright

from utils.config import BASE_URL, BROWSER, HEADLESS
from pages.login_page import LoginPage
from test_data.users import VALID_USER


# 🔹 1. Браузер на всю сессию
@pytest.fixture(scope="session")
def browser_instance():
    playwright = sync_playwright().start()

    browser = getattr(playwright, BROWSER).launch(
        headless=HEADLESS
    )

    yield browser

    browser.close()
    playwright.stop()


# 🔹 2. Новая страница на каждый тест
@pytest.fixture(scope="function")
def page(browser_instance):
    context = browser_instance.new_context()
    page = context.new_page()

    yield page

    context.close()


# 🔹 3. Уже залогиненный пользователь
@pytest.fixture(scope="function")
def logged_in_page(page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login(
        VALID_USER["username"],
        VALID_USER["password"]
    )

    page.wait_for_url("**/inventory.html")

    return page