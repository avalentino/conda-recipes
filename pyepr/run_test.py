#!/usr/bin/env python

import os
import sys
import unittest

import epr

sys.path.append(os.path.join(os.environ['SRC_DIR'], 'tests'))
from test_all import *

print('PyEPR: %s' % epr.__version__)
print('EPR API: %s' % epr.EPR_C_API_VERSION)
print('Python: %s' % sys.version)

unittest.main(verbosity=2)
