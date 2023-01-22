from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.driver.current_url
        assert self.url == 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/', 'Неверный URL формы логина'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_one_element_present(*LoginPageLocators.LOGIN_FORM), 'Нет формы авторизации'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_one_element_present(*LoginPageLocators.REGISTER_FORM), 'Нет формы регистрации'

