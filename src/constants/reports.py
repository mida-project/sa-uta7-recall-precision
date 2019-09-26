#!/usr/bin/env python
#coding=utf-8

"""
reports.py: serving the purpose of reporting both confusion matrix
            and performance metrics.
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
import logging

from os import path

# The current folder path.
basePath = os.path.dirname(__file__)

# The path to the repository "src" folder.
joinRepoSrcPath = os.path.join(basePath, '..')
pathRepoSrcAbsPath = os.path.abspath(joinRepoSrcPath)
# Add the directory containing the module to
# the Python path (wants absolute paths).
sys.path.append(pathRepoSrcAbsPath)

# Appending constants path
strcPath = os.path.join(joinRepoSrcPath, 'structures')
strcAbsPath = os.path.abspath(strcPath)
sys.path.append(strcAbsPath)
sys.path.insert(0, strcAbsPath)

# Importing available variables
from severities import *

# Appending techniques path
techsPath = os.path.join(joinRepoSrcPath, 'techniques')
techsAbsPath = os.path.abspath(techsPath)
sys.path.append(techsAbsPath)
sys.path.insert(0, techsAbsPath)

# Importing available techniques
from evaluations import *

print(arr_birads_real_l)
print(arr_birads_phys_l)

eval_birads_real_phys_l = evalModelSpecific(arr_birads_real_l, arr_birads_phys_l)

print(eval_birads_real_phys_l)

# ==================== END File ==================== #