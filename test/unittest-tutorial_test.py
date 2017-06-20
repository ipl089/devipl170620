# -*- coding:utf-8 -*-

import unittest
import os
import glob
import importlib


def suite():
    suite = unittest.TestSuite()
    dirname = os.path.abspath(os.path.dirname(__file__))
    pathname = dirname + os.sep + 'test*' + os.extsep + 'py'
    for path in glob.glob(pathname):
        basename, ext = os.path.splitext(os.path.basename(path))
        name = 'test.' + basename
        spec = importlib.util.spec_from_file_location(name, path)
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        suite.addTests(unittest.makeSuite(m.TestCase))
    return suite
