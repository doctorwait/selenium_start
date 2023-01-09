from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_backet_button_is_exist(browser):
    browser.get(link)
    try:
        WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "btn-primary")))
    except TimeoutException:
        print('Элемент не был найден.')

if __name__ == '__main__':
    test_backet_button_is_exist()
    # Заметим, что PyCharm подсвечивает жёлтым скобочки, что мол не хватает аргумента. Но всё работает благодаря
    # conftest, как при запуске из терминала, так и напрямую из файла.
