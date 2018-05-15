class BasePage(object):
    BASE_URL = 'http://ok.ru/'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = f'{self.BASE_URL}{self.PATH}'
        self.driver.get(url)
        self.driver.maximize_window()


