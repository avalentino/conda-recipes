#!/usr/bin/env python

import os
import sys
import shutil
import unittest

import hashsum

print('hashsum: v%s' % hashsum.VERSION)
print('Python: %s' % sys.version)

shutil.copytree(os.path.join(os.environ['SRC_DIR'], 'tests'), 'tests')

from tests.test_hashsum import *

try:
    unittest.main(verbosity=2)
finally:
    shutil.rmtree('tests')
