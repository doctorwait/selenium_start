from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def is_not_item_present_in_basket(self):
        return super().is_not_element_present(*BasketPageLocators.ITEM_PRESENTED_IN_BASKET)

    def is_text_about_emptiness_present(self):
        txt = self.driver.find_element(*BasketPageLocators.TEXT_ABOUT_BASKET_EMPTINESS).text
        needed = 'Ваша корзина пуста'
        assert needed in txt, "Текста 'Ваша корзина пуста' на странице нет."
