#!/usr/bin/env python
#coding=utf-8

"""
severities.py: the set of arrays for severity measures.
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
consPath = os.path.join(joinRepoSrcPath, 'constants')
consAbsPath = os.path.abspath(consPath)
sys.path.append(consAbsPath)
sys.path.insert(0, consAbsPath)

# Importing available variables
from sheets import *

import numpy as np

arr_birads_assis_l = df_birads_assis_l.values
arr_birads_assis_m = df_birads_assis_m.values
arr_birads_assis_h = df_birads_assis_h.values

arr_birads_crrnt_l = df_birads_crrnt_l.values
arr_birads_crrnt_m = df_birads_crrnt_m.values
arr_birads_crrnt_h = df_birads_crrnt_h.values

arr_birads_phys_l = df_birads_phys_l.values
arr_birads_phys_m = df_birads_phys_m.values
arr_birads_phys_h = df_birads_phys_h.values

arr_birads_real_l = df_birads_real_l.values
arr_birads_real_m = df_birads_real_m.values
arr_birads_real_h = df_birads_real_h.values