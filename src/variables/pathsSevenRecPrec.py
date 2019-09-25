#!/usr/bin/env python
#coding=utf-8

"""
pathsSevenRecPrec.py: The paths file of the variables for the 7th
                      Recall & Precision Problem statistical analysis.
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
import json
import sys
import requests

from os import path
from pprint import pprint

# The current folder path.
basePath = os.path.dirname(__file__)

# The path to the repository "src" folder.
srcPath = os.path.join(basePath, '..')
srcAbsPath = os.path.abspath(srcPath)
# Add the directory containing the module to
# the Python path (wants absolute paths).
sys.path.append(srcAbsPath)

# The path to the repository "src" folder.
repoPath = os.path.join(basePath, '..', '..')
repoAbsPath = os.path.abspath(repoPath)
# Add the directory containing the module to
# the Python path (wants absolute paths).
sys.path.append(repoAbsPath)

# The path to the repository "root" folder. Mainly,
# this will put us at the `Git` folder level.
rootPath = os.path.join(basePath, '..', '..', '..')
rootAbsPath = os.path.abspath(rootPath)
sys.path.append(rootAbsPath)

# Appending methods path.
methsPath = os.path.join(srcPath, 'methods')
methsAbsPath = os.path.abspath(methsPath)
sys.path.append(methsAbsPath)

# Appending tests path.
testsPath = os.path.join(srcPath, 'tests')
testsAbsPath = os.path.abspath(testsPath)
sys.path.append(testsAbsPath)

# Appending uta7-statistical-analysis-charts path.
uta7sacPath = os.path.join(rootAbsPath, 'uta7-statistical-analysis-charts')
uta7sacAbsPath = os.path.abspath(uta7sacPath)
sys.path.append(uta7sacAbsPath)

# Appending UTA7 - SAC: Src path.
uta7sacSrcPath = os.path.join(uta7sacAbsPath, 'src', '')
uta7sacSrcAbsPath = os.path.abspath(uta7sacSrcPath)
sys.path.append(uta7sacSrcAbsPath)

# Appending UTA7 - SAC: Assets path.
uta7sacAssestsPath = os.path.join(uta7sacAbsPath, 'assets', '')
uta7sacAssestsAbsPath = os.path.abspath(uta7sacAssestsPath)
sys.path.append(uta7sacAssestsAbsPath)

# ============================== #
#       FILE & Folder NAMES      #
# ============================== #

ext101 = '.txt'
ext102 = '.json'
ext103 = '.dcm'
ext104 = '.csv'
ext105 = '.html'
ext106 = '.png'

mul001 = '*' + ext101
mul002 = '*' + ext102

scp01 = '_'
scp02 = '-'

pn007 = 'precision_heatmap_assis'
pn008 = 'precision_heatmap_real'

pnc007 = pn007 + ext106
pnc008 = pn008 + ext106

# ============================== #
# ============================== #

# ============================== #
# ============================== #
#              PATHS             #
# ============================== #
# ============================== #

# ============================== #
#         PATHS - Charts         #
# ============================== #

# Precision Heatmap
fp307 = os.path.join(uta7sacAssestsAbsPath , pnc007)
fp308 = os.path.join(uta7sacAssestsAbsPath , pnc008)

# ============================== #
# ============================== #

# ============================== #
# ============================== #
#              LINKS             #
# ============================== #
# ============================== #

lnk001 = ""

# ============================== #
# ============================== #

# ==================== END File ==================== #