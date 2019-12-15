from sat.helpers import *
from sat import run_browser
from sat.should_frame.should_be import *
from selenium.common.exceptions import NoSuchElementException


class Element(object):
    """Базовый класс для всех элементов"""
    _driver = run_browser.driver
    web_element = lambda self: self._driver.find_element(self.how, self.locator)
    rus_name = None  # русское название элемента в Page
    how = None  # как ищем локатор
    locator = None  # локатор элемента

    def __str__(self):
        return 'Базовый элемент'

    def __init__(self, how, locator, rus_name):
        self.how = how
        self.locator = locator
        self.rus_name = rus_name

    def click(self):
        """Клик по элементу"""
        self.web_element().click()
        log('Кликнули по элементу "{0}"-"{1}" с локатором: "{2}"'.format(self.__str__(), self.rus_name,
                                                                           self.locator))

    @property
    def is_displayed(self):
        """Видимость элемента"""
        result = False
        try:
            return self.web_element().is_displayed()
        except NoSuchElementException:
            return result

    def should_be(self, *cond, desc=None, wait_time=5):
        """Вход в фреймворк с умным ожиданием"""
        should_framework(element=self, desc=desc, wait_time=wait_time, *cond)
        return self
