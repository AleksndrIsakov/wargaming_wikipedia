_BASE_URL = "https://en.wikipedia.org"


class BasePage(object):
    url = _BASE_URL

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.url)
        return self
