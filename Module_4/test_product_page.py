import pytest
import time

from .pages.product_page import ProductPage

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


@pytest.mark.parametrize('link', promo_links)
def test_guest_can_add_product_to_basket(driver, link):
    # link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    # link2 = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(driver, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.is_alerts_presented()
    page.particular_item_was_added()
    # time.sleep(600)
    page.price_verifier()

# @pytest.mark.parametrize('link', ["okay_link", pytest.param("bugged_link", marks=pytest.mark.xfail), "okay_link"])


def test_guest_should_see_login_link_on_product_page(driver):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(driver, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(driver):
    link = 'https://selenium1py.pythonanywhere.com/ru/catalogue/'
    page = ProductPage(driver, link)
    page.open()
    page.go_to_login_page()
