#!/usr/bin/env python

import os
import sys
import shutil
import unittest

import epr

print('PyEPR: %s' % epr.__version__)
print('EPR API: %s' % epr.EPR_C_API_VERSION)
print('Python: %s' % sys.version)

shutil.copy(os.path.join(os.environ['SRC_DIR'], 'tests', 'test_all.py'), '.')

from test_all import *

try:
    unittest.main(verbosity=2)
finally:
    os.remove(TEST_PRODUCT)
    os.remove('test_all.py')
