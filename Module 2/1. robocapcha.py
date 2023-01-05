from selenium import webdriver
import math
import time
with webdriver.Chrome() as browser:
    browser.get('https://suninjuly.github.io/math.html')
    item_x = browser.find_element(by='css selector', value='[id="input_value"]')
    solution = str(math.log(abs(12*math.sin(int(item_x.text)))))
    answer = browser.find_element(by='id', value='answer')
    answer.send_keys(solution)
    check = browser.find_element(by='id', value='robotCheckbox')
    check.click()
    radio = browser.find_element(by='css selector', value='.form-check-input[value="robots"]')
    radio.click()
    send = browser.find_element(by='class name', value='btn')
    send.click()
    time.sleep(5)



