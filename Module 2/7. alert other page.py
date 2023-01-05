from selenium import webdriver
import math
import time

with webdriver.Chrome() as browser:
    browser.get('http://suninjuly.github.io/redirect_accept.html')
    browser.find_element(by='class name', value='trollface').click()
    browser.switch_to.window(browser.window_handles[1])
    x = int(browser.find_element(by='id', value='input_value').text)
    res = str(math.log(abs(12 * math.sin(x))))
    browser.find_element(by='id', value='answer').send_keys(res)
    browser.find_element(by='class name', value='btn').click()
    print(browser.window_handles)

    time.sleep(5)