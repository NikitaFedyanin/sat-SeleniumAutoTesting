from selenium import *
from sat import run_browser


class Element(object):
    driver = run_browser.driver
    locator = None
    rus_name = None
    how = None

    def __init__(self, how, locator, rus_name):
        self.how = how
        self.locator = locator
        self.rus_name = rus_name

    def click(self):
        elm = self.driver.find_element(self.how, self.locator)
        elm.click()
