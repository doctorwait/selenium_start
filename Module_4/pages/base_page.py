from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import math
import time


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.driver = browser
        self.url = url
        self.driver.implicitly_wait(timeout)

    def open(self):
        self.driver.get(self.url)

    def is_one_element_present(self, by, value):
        try:
            self.driver.find_element(by=by, value=value)
        except NoSuchElementException as ex:
            print(ex.msg, 'Такого элемента нет.')
            return False
        except:
            return False
        return True

    def find_list_of_elements(self, by, value):
        return self.driver.find_elements(by=by, value=value)

    def is_not_element_present(self, how, what, timeout=4):
        """
        Проверяет, что элемент не появляется на странице в течение заданного времени. Упадет, как только увидит искомый
        элемент. Не появился: успех, тест зеленый.
        """
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        """
        Когда мы хотим проверить, что какой-то элемент исчезает. Будет ждать до тех пор, пока элемент не исчезнет.
        """
        try:
            WebDriverWait(self.driver, timeout, 1, (TimeoutException, )).until_not(
                EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def solve_quiz_and_get_code(self):
        alert = self.driver.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        time.sleep(5)
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
