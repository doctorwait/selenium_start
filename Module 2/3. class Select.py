import selenium.webdriver.support.select
from selenium import webdriver
import time

with webdriver.Chrome() as browser:
    browser.get('https://suninjuly.github.io/selects2.html')
    x = browser.find_element(by='css selector', value='#num1')
    y = browser.find_element(by='css selector', value='#num2')
    summary = int(x.text) + int(y.text)
    lst = selenium.webdriver.support.select.Select(browser.find_element(by='tag name', value='select'))
    lst.select_by_value(str(summary))
    btn = browser.find_element(by='class name', value='btn')
    btn.click()
    time.sleep(5)
