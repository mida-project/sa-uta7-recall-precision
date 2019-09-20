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
joinRepoSrcPath = os.path.join(basePath, '..')
pathRepoSrcAbsPath = os.path.abspath(joinRepoSrcPath)
# Add the directory containing the module to
# the Python path (wants absolute paths).
sys.path.append(pathRepoSrcAbsPath)

# Appending countings path
consPath = os.path.join(joinRepoSrcPath, 'constants')
consAbsPath = os.path.abspath(consPath)
sys.path.append(consAbsPath)
sys.path.insert(0, consAbsPath)

# Importing available countings
from countings import *

import numpy as np

acp001 = np.array([[c_0_0, c_0_1, c_0_2, c_0_3, c_0_4, c_0_5],
                   [c_1_0, c_1_1, c_1_2, c_1_3, c_1_4, c_1_5],
                   [c_2_0, c_2_1, c_2_2, c_2_3, c_2_4, c_2_5],
                   [c_3_0, c_3_1, c_3_2, c_3_3, c_3_4, c_3_5],
                   [c_4_0, c_4_1, c_4_2, c_4_3, c_4_4, c_4_5],
                   [c_5_0, c_5_1, c_5_2, c_5_3, c_5_4, c_5_5]])

acp002 = np.array([[p_0_0, p_0_1, p_0_2, p_0_3, p_0_4, p_0_5],
                   [p_1_0, p_1_1, p_1_2, p_1_3, p_1_4, p_1_5],
                   [p_2_0, p_2_1, p_2_2, p_2_3, p_2_4, p_2_5],
                   [p_3_0, p_3_1, p_3_2, p_3_3, p_3_4, p_3_5],
                   [p_4_0, p_4_1, p_4_2, p_4_3, p_4_4, p_4_5],
                   [p_5_0, p_5_1, p_5_2, p_5_3, p_5_4, p_5_5]])

# ==================== END File ==================== #