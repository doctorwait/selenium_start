from selenium.common import NoSuchElementException


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
