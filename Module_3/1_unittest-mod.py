import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class First(unittest.TestCase):
    def checker(self):
        browser = webdriver.Chrome()
        browser.get('http://suninjuly.github.io/registration1.html')  # или browser.get(link2) для другой странички

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
        a = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", a)

    def checker2(self):
        browser = webdriver.Chrome()
        browser.get('http://suninjuly.github.io/registration2.html')  # или browser.get(link2) для другой странички

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
        a = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", a)


unittest.main()
