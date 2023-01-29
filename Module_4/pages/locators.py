from selenium.webdriver.common.by import By
# каждый селектор — это пара: как искать и что искать.


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    REGISTRATION_LINK = (By.ID, "registration_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')


class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    ITEM_ADDED_ALERT = (By.CLASS_NAME, 'alertinner')
    CURRENT_ITEM_NAME = (By.CSS_SELECTOR, '.product_main > h1')
    CURRENT_ITEM_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')


class ForDisappearPageLocators:
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success:nth-child(1)')


class BasePageLocators:
    LOGIN_LINK = (By.ID, "login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    GO_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-group>a')


class BasketPageLocators:
    ITEM_PRESENTED_IN_BASKET = (By.CLASS_NAME, 'basket_summary')
    TEXT_ABOUT_BASKET_EMPTINESS = (By.CSS_SELECTOR, '#content_inner > p')


