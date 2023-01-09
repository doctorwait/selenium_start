from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# список всех возможных атрибутов для поиска элементов
names = ["id", "name", "xpath", "link text", "partial link text", "tag name", "class name", "css selector"]

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(by='tag name', value='input')
    input1.send_keys("Ivan")
    input2 = browser.find_element(by='name', value='last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element(by='class name', value='city')
    input3.send_keys("Smolensk")
    input4 = browser.find_element(by='id', value='country')
    input4.send_keys("Russia")
    button = browser.find_element(by='css selector', value="button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
