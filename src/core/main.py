#!/usr/bin/env python
#coding=utf-8

"""
main.py: When creating a Python module, it is common to make
         the module execute some functionality (usually contained
         in a main function) when run as the entry point of
         the program.
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

# Appending variables path
varsPath = os.path.join(joinRepoSrcPath, 'variables')
varsAbsPath = os.path.abspath(varsPath)
sys.path.append(varsAbsPath)
sys.path.insert(0, varsAbsPath)

# Importing available variables
from baseSevenRecPrec import *
from messagesSevenRecPrec import *
from pathsSevenRecPrec import *

# Appending methods path
methodsPath = os.path.join(joinRepoSrcPath, 'methods')
methodsAbsPath = os.path.abspath(methodsPath)
sys.path.append(methodsAbsPath)
sys.path.insert(0, methodsAbsPath)

# Importing available methods
from classifications import *

# Appending structures path
strcPath = os.path.join(joinRepoSrcPath, 'structures')
strcAbsPath = os.path.abspath(strcPath)
sys.path.append(strcAbsPath)
sys.path.insert(0, strcAbsPath)

# Importing available structures
from counters import *

# Appending techniques path
techsPath = os.path.join(joinRepoSrcPath, 'techniques')
techsAbsPath = os.path.abspath(techsPath)
sys.path.append(techsAbsPath)
sys.path.insert(0, techsAbsPath)

# Importing available techniques
from confusions import *
from evaluations import *

# Appending tests path
testsPath = os.path.join(joinRepoSrcPath, 'tests')
testsAbsPath = os.path.abspath(testsPath)
sys.path.append(testsAbsPath)
sys.path.insert(0, testsAbsPath)

# Importing available tests

# ============================== #
# ============================== #

# see: sentry.io
import sentry_sdk
sentry_sdk.init(lnk001)

# ============================== #
# ============================== #
# ============================== #
# ============================== #

# ============================== #
# ============================== #
#       VARIABLES ASSIGNMENT     #
# ============================== #
# ============================== #

# Classifications: Physician + Assistant vs Real
arr_count_class_001 = acc001

# Classifications: Physician vs Real
arr_count_class_002 = acc002

# ============================== #
# ============================== #

def main():
  confMatrixHeatmapToHtml(arr_count_class_001, fp307)
  confMatrixHeatmapToHtml(arr_count_class_002, fp308)

if __name__ == '__main__':
  main()

# ==================== END File ==================== #