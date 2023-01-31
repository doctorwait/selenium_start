from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

import pytest
import time
# Пример того, как работает паттерн.

@pytest.mark.login_guest
class TestLoginFromMainPage:
    main_page_link = "http://selenium1py.pythonanywhere.com/"

    def test_guest_can_go_to_login_page(self, driver):
        page = MainPage(driver, self.main_page_link)
        page.open()
        # Для первого способа:
        # login_page = page.go_to_login_page()
        # login_page.should_be_login_link()
        page.go_to_login_page()
        print(driver.current_url)
        login_page = LoginPage(driver, driver.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, driver):
        page = MainPage(driver, self.main_page_link)
        page.open()
        page.should_be_login_link()


def test_guest_can_go_to_login_page(driver):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(driver, link)
    page.open()
    # Для первого способа:
    # login_page = page.go_to_login_page()
    # login_page.should_be_login_link()
    page.go_to_login_page()
    print(driver.current_url)
    login_page = LoginPage(driver, driver.current_url)
    login_page.should_be_login_page()


def test_should_be_login_page(driver):
    link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
    page = LoginPage(driver, link)
    page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(driver):
    link = 'https://selenium1py.pythonanywhere.com/ru/'
    page = MainPage(driver, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(driver, driver.current_url)
    basket_page.is_not_item_present_in_basket()
    basket_page.is_text_about_emptiness_present()
    