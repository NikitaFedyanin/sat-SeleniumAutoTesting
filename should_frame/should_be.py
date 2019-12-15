from sat.should_frame.conditions import *
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime


def should_framework(*cond, element, desc, wait_time):
    """основной метод вычисления заданного состояния с оджиданием"""
    element = element
    web_element = element.web_element
    conditions = [i() for i in cond]
    wait_time = wait_time
    desc = desc

    for condition in conditions:
        assert isinstance(condition, Condition), 'в should_be передано не состояние'
        if condition.__str__() == 'displayed':
            if not desc:
                desc = 'Элемент "{0}"-"{1}" с локатором: "{2}" не отображается\n'.format(element.__str__(),
                                                                                         element.rus_name,
                                                                                         element.locator)
            wait_action(condition=lambda: web_element().is_displayed(), desc=desc, wait_time=wait_time)


def wait_action(condition, desc, wait_time):
    """Выполнение условия с ожиданием"""
    start_time = datetime.now()
    while True:
        try:
            if condition():
                break
        except NoSuchElementException:
            diff_second = (datetime.now() - start_time).seconds
            if diff_second > wait_time:
                raise AssertionError(desc) from None
