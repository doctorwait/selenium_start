from .pages.product_page import ProductPage
import time


def test_guest_can_add_product_to_basket(driver):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    link2 = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(driver, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    time.sleep(5)
    page.is_alerts_presented()
    page.particular_item_was_added()
    page.price_verifier()




