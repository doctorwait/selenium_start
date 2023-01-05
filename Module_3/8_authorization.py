import pytest
from selenium import webdriver
import time
import math


links_list = ['https://stepik.org/lesson/236895/step/1',
                'https://stepik.org/lesson/236896/step/1',
                'https://stepik.org/lesson/236897/step/1',
                'https://stepik.org/lesson/236898/step/1',
                'https://stepik.org/lesson/236899/step/1',
                'https://stepik.org/lesson/236903/step/1',
                'https://stepik.org/lesson/236904/step/1',
                'https://stepik.org/lesson/236905/step/1']


@pytest.fixture(scope="function")
def driver():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('links', links_list)
def test_links(driver, links):
    driver.get(links)
    time.sleep(5)
    button_login = driver.find_element(by='id', value='ember32')
    button_login.click()
    driver.switch_to.active_element
    login = driver.find_element(by='name', value='login')
    login.send_keys('prosnites@yandex.ru')
    password = driver.find_element(by='name', value='password')
    password.send_keys('Ebalvr0tSteps')
    button_enter = driver.find_element(by='css selector', value='#login_form > button')
    button_enter.click()

    time.sleep(5)
    answer = math.log(int(time.time()))
    driver.find_element(by='css selector', value='.ember-text-area').send_keys(answer)
    driver.find_element(by='css selector', value='.submit-submission').click()
    time.sleep(5)
    msg = driver.find_element(by='css selector', value='.smart-hints__hint').text
    assert msg == 'Correct!', f'Тест по ссылке {links} упал.'
    time.sleep()

