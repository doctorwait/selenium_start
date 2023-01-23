from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        button = self.driver.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        button.click()

    def is_alerts_presented(self):
        list_of_alerts = self.find_list_of_elements(*ProductPageLocators.ITEM_ADDED_ALERT)
        print(list_of_alerts)
        assert len(list_of_alerts) > 0, "Сообщений о добавлении товара нет."

    def particular_item_was_added(self):
        reference = "The shellcoder's handbook"
        text = self.find_list_of_elements(*ProductPageLocators.ITEM_ADDED_ALERT)[0].text
        assert reference in text, "В корзину был добавлен не тот товар."

    def price_verifier(self):
        reference = '9.99'
        price = self.find_list_of_elements(*ProductPageLocators.ITEM_ADDED_ALERT)[2].text
        assert reference in price, "Цена не совпадает с необходимой."

