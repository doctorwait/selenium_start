from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.for_disappear_page import ForDisappearPage
from .pages.login_page import LoginPage

import pytest
import time

promo_links = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
               pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                            marks=pytest.mark.xfail),
               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope='function', autouse=True)
    def setup_class(self, driver):
        link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
        page = LoginPage(driver, link)
        page.open()
        page.register_new_user(email=str(time.time()) + "@fakemail.org", password='123qwerty!')
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, driver):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ForDisappearPage(driver, link)
        page.open()
        page.user_cant_see_success_message(
            'Сообщение об успешном добавлении товара в корзину появилось, хотя кнопку не нажимали.')

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, driver):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/'
        page = ProductPage(driver, link)
        page.open()
        page.add_to_cart()
        page.is_alerts_presented()
        page.particular_item_was_added()
        page.price_verifier()


@pytest.mark.need_review
@pytest.mark.parametrize('link', promo_links)
def test_guest_can_add_product_to_basket(driver, link):
    page = ProductPage(driver, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.is_alerts_presented()
    page.particular_item_was_added()
    page.price_verifier()


def test_guest_should_see_login_link_on_product_page(driver):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(driver, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(driver):
    link = 'https://selenium1py.pythonanywhere.com/ru/catalogue/'
    page = ProductPage(driver, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(driver):
    link = 'https://selenium1py.pythonanywhere.com/ru/catalogue/the-girl-who-played-with-non-fire_203/'
    page = ProductPage(driver, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(driver, driver.current_url)
    basket_page.is_not_item_present_in_basket()
    basket_page.is_text_about_emptiness_present()


