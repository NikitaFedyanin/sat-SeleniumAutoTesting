from selenium import *
from seleniumpagefactory import *

class Page:
    driver = None


    def __init__(self):
        pass

    def __get__(self, instance, owner):
        if not instance:
            return None
        else:
            self.driver = instance.driver