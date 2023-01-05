from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    link2 = 'http://suninjuly.github.io/registration2.html'
    browser = webdriver.Chrome()
    browser.get(link)  # или browser.get(link2) для другой странички

    input1 = browser.find_element(by='css selector', value='.first[required=""]')
    input1.send_keys("Ivan")
    input2 = browser.find_element(by='css selector', value='.second[required=""]')
    input2.send_keys("Petrov")
    input3 = browser.find_element(by='css selector', value='.third[required=""]')
    input3.send_keys("Smolensk")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)  # Ошибка NoSuchElementException лучше видна без этого времени ожидания

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
