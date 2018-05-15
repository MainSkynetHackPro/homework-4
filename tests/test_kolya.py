import unittest

from driver import get_driver
from pages.auth_page import AuthPage


class TestKolya(unittest.TestCase):

    def setUp(self):
        self.driver = get_driver()

    def tearDown(self):
        self.driver.quit()

    def test_create_mood(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_page.set_login('123')
        auth_page.set_password('312')
        auth_page.login()

