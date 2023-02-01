from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.driver.current_url
        ordinary_url = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
        # Сравним в отдельности две части строки, чтобы избежать конфликтов с локалью и http / http(s)
        assert self.url.split('/')[2] == ordinary_url.split('/')[2] and '/'.join(self.url.split('/')[4:]) == '/'.join(
            ordinary_url.split('/')[4:]), 'Неверный URL формы логина'

    def should_be_login_form(self):
        assert self.is_one_element_present(*LoginPageLocators.LOGIN_FORM), 'Нет формы авторизации'

    def should_be_register_form(self):
        assert self.is_one_element_present(*LoginPageLocators.REGISTER_FORM), 'Нет формы регистрации'

    def register_new_user(self, email, password):
        self.driver.find_element(*LoginPageLocators.REGISTER_FORM_INPUT_EMAIL_FIELD).send_keys(email)
        self.driver.find_element(*LoginPageLocators.REGISTER_FORM_INPUT_PASSWORD_FIELD_1).send_keys(password)
        self.driver.find_element(*LoginPageLocators.REGISTER_FORM_INPUT_PASSWORD_FIELD_2).send_keys(password)
        self.driver.find_element(*LoginPageLocators.REGISTER_FINISH_BUTTON).click()



