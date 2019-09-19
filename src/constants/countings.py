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
from sheets import *

# Appending countings path
methsPath = os.path.join(joinRepoSrcPath, 'methods')
methsAbsPath = os.path.abspath(methsPath)
sys.path.append(methsAbsPath)
sys.path.insert(0, methsAbsPath)

# Importing available countings
from classifications import *

# ============================== #
# ============================== #
#     COUNTING TRUE-POSITIVES    #
# ============================== #
# ============================== #

# ============================== #
#             Singles            #
# ============================== #

cltp_0_0 = countLowTruePositives(0, 0, df_birads_real, df_birads_phy)
cmtp_0_0 = countMedTruePositives(0, 0, df_birads_real, df_birads_phy)
chtp_0_0 = countHghTruePositives(0, 0, df_birads_real, df_birads_phy)

cltp_1_1 = countLowTruePositives(1, 1, df_birads_real, df_birads_phy)
cmtp_1_1 = countMedTruePositives(1, 1, df_birads_real, df_birads_phy)
chtp_1_1 = countHghTruePositives(1, 1, df_birads_real, df_birads_phy)

cltp_2_2 = countLowTruePositives(2, 2, df_birads_real, df_birads_phy)
cmtp_2_2 = countMedTruePositives(2, 2, df_birads_real, df_birads_phy)
chtp_2_2 = countHghTruePositives(2, 2, df_birads_real, df_birads_phy)

cltp_3_3 = countLowTruePositives(3, 3, df_birads_real, df_birads_phy)
cmtp_3_3 = countMedTruePositives(3, 3, df_birads_real, df_birads_phy)
chtp_3_3 = countHghTruePositives(3, 3, df_birads_real, df_birads_phy)

cltp_4_4 = countLowTruePositives(4, 4, df_birads_real, df_birads_phy)
cmtp_4_4 = countMedTruePositives(4, 4, df_birads_real, df_birads_phy)
chtp_4_4 = countHghTruePositives(4, 4, df_birads_real, df_birads_phy)

cltp_5_5 = countLowTruePositives(5, 5, df_birads_real, df_birads_phy)
cmtp_5_5 = countMedTruePositives(5, 5, df_birads_real, df_birads_phy)
chtp_5_5 = countHghTruePositives(5, 5, df_birads_real, df_birads_phy)

# ============================== #

# ============================== #
#             Totals             #
# ============================== #

c_0_0 = cltp_0_0 + cmtp_0_0 + chtp_0_0
c_1_1 = cltp_1_1 + cmtp_1_1 + chtp_1_1
c_2_2 = cltp_2_2 + cmtp_2_2 + chtp_2_2
c_3_3 = cltp_3_3 + cmtp_3_3 + chtp_3_3
c_4_4 = cltp_4_4 + cmtp_4_4 + chtp_4_4
c_5_5 = cltp_5_5 + cmtp_5_5 + chtp_5_5

# ============================== #

# ============================== #
# ============================== #

# ============================== #
# ============================== #
#     COUNTING TRUE-NEGATIVES    #
# ============================== #
# ============================== #

# ============================== #
#             Singles            #
# ============================== #

# ============================== #

# ============================== #
#             Totals             #
# ============================== #

# ============================== #

# ============================== #
# ============================== #

c_0_1 = 1
c_0_2 = 1
c_0_3 = 1
c_0_4 = 1
c_0_5 = 1

c_1_0 = 1

c_1_1 = cltp_1_1 + cmtp_1_1 + chtp_1_1

c_1_2 = 1
c_1_3 = 1
c_1_4 = 1
c_1_5 = 1

c_2_0 = 1
c_2_1 = 1

c_2_2 = cltp_2_2 + cmtp_2_2 + chtp_2_2

c_2_3 = 1
c_2_4 = 1
c_2_5 = 1

c_3_0 = 1
c_3_1 = 1
c_3_2 = 1

c_3_3 = cltp_3_3 + cmtp_3_3 + chtp_3_3

c_3_4 = 1
c_3_5 = 1

c_4_0 = 1
c_4_1 = 1
c_4_2 = 1
c_4_3 = 1

c_4_4 = cltp_4_4 + cmtp_4_4 + chtp_4_4

c_4_5 = 1

c_5_0 = 1
c_5_1 = 1
c_5_2 = 1
c_5_3 = 1
c_5_4 = 1

c_5_5 = cltp_5_5 + cmtp_5_5 + chtp_5_5

# ==================== END File ==================== #