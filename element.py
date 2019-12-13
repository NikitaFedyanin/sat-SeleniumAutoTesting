from sat.helpers import *
from sat import run_browser
from sat.should_frame.should_be import *


class Element(object):
    _driver = run_browser.driver
    web_element = lambda self: self._driver.find_element(self._how, self._locator)
    _rus_name = None
    _how = None
    _locator = None

    def __str__(self):
        return 'Базовый элемент'

    def __init__(self, how, locator, rus_name):
        self._how = how
        self._locator = locator
        self._rus_name = rus_name

    def click(self):
        self.web_element().click()
        log('Кликнули по элементу "{0}"-"{1}" с локатором: "{2}"\n'.format(self.__str__(), self._rus_name,
                                                                           self._locator))

    def should_be(self, *cond, desc=None):
        should_framework(self.web_element(), desc, *cond)
