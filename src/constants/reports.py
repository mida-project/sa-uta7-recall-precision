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
import operator

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

arr_birads_real_total = [*arr_birads_real_l, *arr_birads_real_m, *arr_birads_real_h]
arr_birads_phys_total = [*arr_birads_phys_l, *arr_birads_phys_m, *arr_birads_phys_h]

ebrplccm, ebrplcr = evalModelSpecific(arr_birads_real_l, arr_birads_phys_l)
ebrpmccm, ebrpmcr = evalModelSpecific(arr_birads_real_m, arr_birads_phys_m)
ebrphccm, ebrphcr = evalModelSpecific(arr_birads_real_h, arr_birads_phys_h)

ebrptccm, ebrptcr = evalModelSpecific(arr_birads_real_total, arr_birads_phys_total)

eval_birads_real_phys_l_conf_matrix = ebrplccm
eval_birads_real_phys_l_report = ebrplcr

eval_birads_real_phys_m_conf_matrix = ebrpmccm
eval_birads_real_phys_m_report = ebrpmcr

eval_birads_real_phys_h_conf_matrix = ebrphccm
eval_birads_real_phys_h_report = ebrphcr

eval_birads_real_phys_t_conf_matrix = ebrptccm
eval_birads_real_phys_t_report = ebrptcr

# print(eval_birads_real_phys_l_conf_matrix)
# print(eval_birads_real_phys_l_report)

# print(eval_birads_real_phys_m_conf_matrix)
# print(eval_birads_real_phys_m_report)

# print(eval_birads_real_phys_h_conf_matrix)
# print(eval_birads_real_phys_h_report)

# print("========================")

print(eval_birads_real_phys_t_conf_matrix)
print(eval_birads_real_phys_t_report)

# ==================== END File ==================== #