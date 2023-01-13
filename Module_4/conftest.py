import pytest as pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en')


@pytest.fixture(scope="function")
def driver(request):
    user_language = request.config.getoption("language")
    options_firefox = Options()
    options_firefox.set_preference("intl.accept_languages", user_language)
    browser = webdriver.Firefox(options=options_firefox)
    yield browser
    browser.quit()
