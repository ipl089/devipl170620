# -*- coding:utf-8 -*-

import unittest


class TestCase(unittest.TestCase):
    def test_upper(self):
        s = "Hello"
        self.assertEqual(s.upper(), "HELLO")


if __name__ == '__main__':
    unittest.main()
