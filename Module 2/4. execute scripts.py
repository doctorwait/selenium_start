from selenium import webdriver
import time
import math

with webdriver.Chrome() as browser:
    browser.get('https://suninjuly.github.io/execute_script.html')
    x = int(browser.find_element(by='id', value='input_value').text)
    res = str(math.log(abs(12*math.sin(x))))
    browser.execute_script("window.scrollBy(0, 100);")
    browser.find_element(by='id', value='answer').send_keys(res)
    browser.find_element(by='id', value='robotCheckbox').click()
    browser.find_element(by='id', value='robotsRule').click()
    browser.find_element(by='class name', value='btn').click()
    time.sleep(5)
