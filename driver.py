from selenium import webdriver
import os

CHROME_DRIVER = 'chrome'
GECKO_DRIVER = 'firefox'


def get_driver():
    driver = os.environ.get('DRIVER', 'chrome')
    if driver == CHROME_DRIVER:
        return webdriver.Chrome('./chromedriver')
    elif driver == GECKO_DRIVER:
        return webdriver.Firefox(executable_path='./geckodriver')
    else:
        raise Exception('Wrong driver specified, use "%s" or "%s"' % (CHROME_DRIVER, GECKO_DRIVER))
