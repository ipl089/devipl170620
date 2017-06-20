# -*- coding:utf-8 -*-

import unittest
import mymath  # ../src/mymath.py


class TestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(mymath.add(2, 3), 5)


if __name__ == '__main__':
    unittest.main()
