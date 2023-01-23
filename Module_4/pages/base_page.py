import time

from selenium.common import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import math


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
