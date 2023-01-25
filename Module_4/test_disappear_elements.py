from .pages.for_disappear_page import ForDisappearPage
from .pages.locators import ForDisappearPageLocators
import pytest


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(driver):
    page = ForDisappearPage(driver, link)
    page.open()
    page.add_to_cart()
    is_message_present = page.is_not_element_present(*ForDisappearPageLocators.SUCCESS_MESSAGE)
    assert is_message_present, 'Сообщения об успешном добавлении товара в корзину, после нажатия кнопки, нет.'


def test_guest_cant_see_success_message(driver):
    page = ForDisappearPage(driver, link)
    page.open()
    is_message_present = page.is_not_element_present(*ForDisappearPageLocators.SUCCESS_MESSAGE)
    assert is_message_present, 'Сообщение об успешном добавлении товара в корзину появилось, хотя кнопку не нажимали.'


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(driver):
    page = ForDisappearPage(driver, link)
    page.open()
    page.add_to_cart()
    is_message_present = page.is_disappeared(*ForDisappearPageLocators.SUCCESS_MESSAGE)
    assert is_message_present, 'Сообщение не исчезает со временем'

