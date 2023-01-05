import time
from selenium import webdriver

# Класс By позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By

# инициализирует драйвер браузера.
driver = webdriver.Chrome()
time.sleep(5)

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("https://stepik.org/lesson/25969/step/12")
time.sleep(10)

# Метод find_element позволяет найти нужный элемент на сайте, указав путь к нему. Метод принимает в качестве аргументов
# способ поиска и значение, по которому мы будем искать. Ищем поле для ввода текста.
textarea = driver.find_element(By.CSS_SELECTOR, ".textarea")
time.sleep(5)

# Напишем текст ответа в найденное поле
textarea.send_keys("get()")
time.sleep(5)

# Найдем кнопку, которая отправляет введенное решение
submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")
time.sleep(5)

# Скажем драйверу, что нужно нажать на кнопку.
submit_button.click()
time.sleep(5)

# Закрыть окно браузера
driver.quit()