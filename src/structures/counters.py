#!/usr/bin/env python
#coding=utf-8

"""
.py:
"""

__author__      = "Francisco Maria Calisto"
__maintainer__  = "Francisco Maria Calisto"
__email__       = "francisco.calisto@tecnico.ulisboa.pt"
__license__     = "MIT"
__version__     = "1.0.0"
__status__      = "Development"
__copyright__   = "Copyright 2019, Instituto Superior Técnico (IST)"
__credits__     = [
  "Bruno Oliveira",
  "Carlos Santiago",
  "Jacinto C. Nascimento",
  "Pedro Miraldo",
  "Nuno Nunes"
]

import os
import sys

from os import path

# The current folder path.
basePath = os.path.dirname(__file__)

# The path to the repository "src" folder.
joinPath = os.path.join(basePath, '..')
pathAbsPath = os.path.abspath(joinPath)
# Add the directory containing the module to
# the Python path (wants absolute paths).
sys.path.append(pathAbsPath)

# Appending countings path
consPath = os.path.join(joinPath, 'constants')
consAbsPath = os.path.abspath(consPath)
sys.path.append(consAbsPath)
sys.path.insert(0, consAbsPath)

# Importing available countings
from countings import *

import numpy as np

acp = np.array([[c_0_0, c_0_1, c_0_2, c_0_3, c_0_4, c_0_5],
                [c_1_0, c_1_1, c_1_2, c_1_3, c_1_4, c_1_5],
                [c_2_0, c_2_1, c_2_2, c_2_3, c_2_4, c_2_5],
                [c_3_0, c_3_1, c_3_2, c_3_3, c_3_4, c_3_5],
                [c_4_0, c_4_1, c_4_2, c_4_3, c_4_4, c_4_5],
                [c_5_0, c_5_1, c_5_2, c_5_3, c_5_4, c_5_5]])

# ==================== END File ==================== #