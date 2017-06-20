# -*- coding:utf-8 -*-

import unittest
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtTest import QTest


if QApplication.instance() is None:
    import sys
    app = QApplication(sys.argv)


class TestCase(unittest.TestCase):
    def test_key_input(self):
        w = QLineEdit()
        QTest.keyClicks(w, "Hello")
        self.assertEqual(w.text(), "Hello")


if __name__ == '__main__':
    unittest.main()
