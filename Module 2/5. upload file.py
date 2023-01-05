from selenium import webdriver
import time
import os

with webdriver.Chrome() as browser:
    browser.get('http://suninjuly.github.io/file_input.html')
    browser.find_element(by='name', value='firstname').send_keys('one')
    browser.find_element(by='name', value='lastname').send_keys('two')
    browser.find_element(by='name', value='email').send_keys('three')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, '1.txt')
    browser.find_element(by='id', value='file').send_keys(file_path)
    browser.find_element(by='tag name', value='button').click()
    time.sleep(5)
