from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        button = self.driver.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        button.click()

    def is_alerts_presented(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "messages")))
        list_of_alerts = self.find_list_of_elements(*ProductPageLocators.ITEM_ADDED_ALERT)
        print(list_of_alerts)
        assert len(list_of_alerts) > 0, "Сообщений о добавлении товара нет."

    def particular_item_was_added(self):
        reference = self.driver.find_element(*ProductPageLocators.CURRENT_ITEM_NAME).text + ' has been added to your basket.'
        text = self.find_list_of_elements(*ProductPageLocators.ITEM_ADDED_ALERT)[0].text
        assert reference == text, "В корзину был добавлен не тот товар."

    def price_verifier(self):
        reference = 'Your basket total is now ' + self.driver.find_element(*ProductPageLocators.CURRENT_ITEM_PRICE).text
        price = self.find_list_of_elements(*ProductPageLocators.ITEM_ADDED_ALERT)[2].text
        assert reference in price, "Цена не совпадает с необходимой."




