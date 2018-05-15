# -*- coding: utf-8 -*-

import unittest
from tests.test_kolya import TestKolya
from tests.test_kostya import TestKostya
from tests.test_max import TestMax

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(TestKolya),
        unittest.makeSuite(TestKostya),
        unittest.makeSuite(TestMax),
    ))
    result = unittest.TextTestRunner().run(suite)