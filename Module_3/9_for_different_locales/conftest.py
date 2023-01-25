from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import pytest
import os

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
                     help="Выберите локаль (на каком языке).")

@pytest.fixture(scope="function")
def driver(request):
    user_language = request.config.getoption("language")
    options_firefox = Options()
    options_firefox.binary_location = '/snap/firefox/2154/usr/lib/firefox/firefox'
    options_firefox.set_preference("intl.accept_languages", user_language)
    browser = webdriver.Firefox(options=options_firefox)
    yield browser
    browser.quit()
