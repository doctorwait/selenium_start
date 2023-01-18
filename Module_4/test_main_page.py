from .pages.main_page import MainPage
from .pages.login_page import LoginPage
# Пример того, как работает паттерн.


def test_guest_can_go_to_login_page(driver):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(driver, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()


def test_should_be_login_page(driver):
    link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
    page = LoginPage(driver, link)
    page.should_be_login_page()
