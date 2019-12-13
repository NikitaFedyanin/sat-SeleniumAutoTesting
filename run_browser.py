from selenium import webdriver

driver = webdriver.Chrome()


class Browser:
    """Запуск браузера"""
    url = None
    instance = None
    driver = None

    def __init__(self, url=None):
        self.driver = driver
        self.url = url
        self._open_url()

    def _open_url(self):
        """Открыть url"""
        self.driver.get('about:blank')
        self.driver.maximize_window()
        self.driver.get(self.url)


def close_window():
    driver.close()
