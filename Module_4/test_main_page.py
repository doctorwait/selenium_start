from .pages.main_page import MainPage
from .pages.login_page import LoginPage
# Пример того, как работает паттерн.


def test_guest_can_go_to_login_page(driver):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(driver, link)
    page.open()
    # Для первого способа:
    # login_page = page.go_to_login_page()
    # login_page.should_be_login_link()
    page.go_to_login_page()
    print(driver.current_url)
    login_page = LoginPage(driver, driver.current_url)
    login_page.should_be_login_page()


def test_should_be_login_page(driver):
    link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
    page = LoginPage(driver, link)
    page.should_be_login_page()
