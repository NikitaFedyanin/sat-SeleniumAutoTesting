"""Модуль с условиями"""


class Condition:
    """Основной класс для проверки типа"""
    pass


class Displayed(Condition):
    """Условие видимости"""

    def __str__(self):
        return "displayed"
