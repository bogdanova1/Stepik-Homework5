from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def find(self, how, what):
        try:
            element = self.browser.find_element(how, what)
        except NoSuchElementException:
            return None
        return element

    def find_all(self, how, what):
        return self.browser.find_elements(how, what)

    @staticmethod
    def find_in_element(parent, locator):
        return parent.find_element_by_CSS_slector(locator)
