from .base_page import BasePage
from .locators import ForDisappearPageLocators


class ForDisappearPage(BasePage):
    def add_to_cart(self):
        button = self.driver.find_element(*ForDisappearPageLocators.ADD_TO_CART_BUTTON)
        button.click()

    def is_message_present(self, tech_msg):
        assert self.is_not_element_present(*ForDisappearPageLocators.SUCCESS_MESSAGE), tech_msg

    def is_message_disappeared(self, tech_msg):
        assert self.is_disappeared(*ForDisappearPageLocators.SUCCESS_MESSAGE), tech_msg

    def user_cant_see_success_message(self, tech_msg):
        self.is_not_element_present(*ForDisappearPageLocators.SUCCESS_MESSAGE)
