from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import math, time


with webdriver.Chrome() as driver:
    driver.get('https://suninjuly.github.io/explicit_wait2.html')
    button = driver.find_element(by='id', value='book')
    WebDriverWait(driver, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    button.click()
    x = int(driver.find_element(by='id', value='input_value').text)
    res = str(math.log(abs(12 * math.sin(x))))
    driver.find_element(by='id', value='answer').send_keys(res)
    driver.find_element(by='id', value='solve').click()
    time.sleep(5)
