from .base_page import BasePage
from .locators import ForDisappearPageLocators


class ForDisappearPage(BasePage):
    def add_to_cart(self):
        button = self.driver.find_element(*ForDisappearPageLocators.ADD_TO_CART_BUTTON)
        button.click()

