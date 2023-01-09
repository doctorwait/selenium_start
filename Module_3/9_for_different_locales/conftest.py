from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox
import pytest


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Выберите локаль (на каком языке).")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    #options = Options()
    #options.add_experimental_option(
    #    'prefs', {'intl.accept_languages': user_language})
    options_firefox = OptionsFirefox()
    options_firefox.set_preference("intl.accept_languages", user_language)
    browser = webdriver.Firefox(options=options_firefox)
    yield browser
    browser.quit()
