#!/usr/bin/env python

import os
import sys
import shutil
import unittest

import hashsum

print('hashsum: v%s' % hashsum.VERSION)
print('Python: %s' % sys.version)

from tests.test_hashsum import *

unittest.main(verbosity=2)
