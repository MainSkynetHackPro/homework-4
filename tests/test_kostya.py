import unittest

from driver import get_driver


class TestKostya(unittest.TestCase):

    def setUp(self):
        self.driver = get_driver()

    def tearDown(self):
        self.driver.quit()

    def test_simple(self):
        self.driver.get("http://park.mail.ru/")
