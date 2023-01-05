# то же самое, что и в 1 робокапче, но значение мы вытаскиваем из атрибута
import selenium.webdriver.support.select
from selenium import webdriver
import time
import math

with webdriver.Chrome() as browser:
    browser.get('http://suninjuly.github.io/get_attribute.html')
    value_elem = browser.find_element(by='id', value='treasure')
    value = value_elem.get_attribute('valuex')  # Применяем метод к веб-элементу!
    solution = str(math.log(abs(12 * math.sin(int(value)))))
    answer = browser.find_element(by='id', value='answer')
    answer.send_keys(solution)
    check = browser.find_element(by='id', value='robotCheckbox')
    check.click()
    radio = browser.find_element(by='id', value='robotsRule')
    radio.click()
    send = browser.find_element(by='class name', value='btn')
    send.click()
    time.sleep(5)
