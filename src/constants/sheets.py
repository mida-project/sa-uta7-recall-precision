#!/usr/bin/env python
#coding=utf-8

"""
sheets.py: to read our data, we are using several datasets. For that,
           we need to read a bunch of csv files. The presented file,
           will serve this purpose. It is here, where we are reading
           our datasets, provinding several variables to be used.
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

pathReposDirname = os.path.dirname(__file__)
joinReposPath = os.path.join(pathReposDirname, '..', '..', '..')
pathReposAbsPath = os.path.abspath(joinReposPath)

sr_dir = os.path.join(pathReposAbsPath, 'sheet-reader')
sys.path.append(sr_dir)
srAbsPath = os.path.abspath(sr_dir)

src_data_dir = os.path.join(srAbsPath, 'data')
sys.path.append(src_data_dir)
srcDataAbsPath = os.path.abspath(src_data_dir)

src_data_tmp_dir = os.path.join(srcDataAbsPath, 'temp')
sys.path.append(src_data_tmp_dir)
srcDataTmpAbsPath = os.path.abspath(src_data_tmp_dir)

# ============================== #
# ============================== #

import pandas as pd

# ============================== #
# ============================== #
# ============================== #
# ============================== #

# ============================== #
# ============================== #
#               PATH             #
# ============================== #
# ============================== #

birads_crrnt_dir = os.path.join(srcDataTmpAbsPath, 'birads_crrnt.csv')
sys.path.append(birads_crrnt_dir)
birads_crrnt_abs_path = os.path.abspath(birads_crrnt_dir)

birads_real_dir = os.path.join(srcDataTmpAbsPath, 'birads_real.csv')
sys.path.append(birads_real_dir)
birads_real_abs_path = os.path.abspath(birads_real_dir)

birads_phy_dir = os.path.join(srcDataTmpAbsPath, 'birads_phy.csv')
sys.path.append(birads_phy_dir)
birads_phy_abs_path = os.path.abspath(birads_phy_dir)

birads_assis_dir = os.path.join(srcDataTmpAbsPath, 'birads_assis.csv')
sys.path.append(birads_assis_dir)
birads_assis_abs_path = os.path.abspath(birads_assis_dir)

# ============================== #
# ============================== #
# ============================== #
# ============================== #

# ============================== #
# ============================== #
#       VARIABLES ASSIGNMENT     #
# ============================== #
# ============================== #

df_birads_assis = pd.read_csv(birads_assis_abs_path, delimiter = ',')
df_birads_crrnt = pd.read_csv(birads_crrnt_abs_path, delimiter = ',')
df_birads_phys = pd.read_csv(birads_phy_abs_path, delimiter = ',')
df_birads_real = pd.read_csv(birads_real_abs_path, delimiter = ',')

# ============================== #
# ============================== #
# ============================== #
# ============================== #

# ============================== #
# ============================== #
#         SPECIFIC ARRAYS        #
# ============================== #
# ============================== #

df_birads_assis_l = df_birads_assis.low
df_birads_assis_m = df_birads_assis.medium
df_birads_assis_h = df_birads_assis.high

df_birads_crrnt_l = df_birads_crrnt.low
df_birads_crrnt_m = df_birads_crrnt.medium
df_birads_crrnt_h = df_birads_crrnt.high

df_birads_phys_l = df_birads_phys.low
df_birads_phys_m = df_birads_phys.medium
df_birads_phys_h = df_birads_phys.high

df_birads_real_l = df_birads_real.low
df_birads_real_m = df_birads_real.medium
df_birads_real_h = df_birads_real.high

# ============================== #
# ============================== #
# ============================== #
# ============================== #

# ==================== END File ==================== #