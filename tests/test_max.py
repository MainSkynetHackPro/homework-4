import unittest

import os
from driver import get_driver
from pages.auth_page import AuthPage
from selenium.webdriver.support.wait import WebDriverWait


class TestMax(unittest.TestCase):
    WRITE_POST_BUTTON = 'posting-form_itx_dec'
    TEXT_FIELD = '//div[@class="posting_itx emoji-tx h-mod js-ok-e ok-posting-handler"]'
    BUTTON_SUBMIT_NOTE = 'posting_f_r'

    LOGIN = os.environ['LOGIN']
    PASSWORD = os.environ['PASSWORD']

    DEFAULT_WAIT_TIME = 10
    MESSAGE = 'msg'

    def setUp(self):
        self.driver = get_driver()

    def tearDown(self):
        self.driver.quit()

    def test_create_mood(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_page.set_login(self.LOGIN)
        auth_page.set_password(self.PASSWORD)
        auth_page.login()

    def get_window_note(self):
        return WebDriverWait(self.driver, self.DEFAULT_WAIT_TIME, 0.1).until(
            lambda d: d.find_element_by_class_name(self.WRITE_POST_BUTTON)
        )

    def get_text_field(self):
        return WebDriverWait(self.driver, self.DEFAULT_WAIT_TIME, 0.1).until(
            lambda d: d.find_element_by_xpath(self.TEXT_FIELD)
        )

    def add_note(self, field, note):
            self.driver.execute_script("arguments[0].textContent = '{}';".format(note), field)

    def test_write_post(self):
        self.test_create_mood()
        window_note = self.get_window_note().click()
        text_field = self.get_text_field()
        self.add_note(text_field, self.MESSAGE)
        self.driver.find_element_by_class_name(self.BUTTON_SUBMIT_NOTE).click()



