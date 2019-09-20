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

cltp_0_0 = countLowTruePositives(0, 0, df_birads_phy, df_birads_real)
cmtp_0_0 = countMedTruePositives(0, 0, df_birads_phy, df_birads_real)
chtp_0_0 = countHghTruePositives(0, 0, df_birads_phy, df_birads_real)

cltp_1_1 = countLowTruePositives(1, 1, df_birads_phy, df_birads_real)
cmtp_1_1 = countMedTruePositives(1, 1, df_birads_phy, df_birads_real)
chtp_1_1 = countHghTruePositives(1, 1, df_birads_phy, df_birads_real)

cltp_2_2 = countLowTruePositives(2, 2, df_birads_phy, df_birads_real)
cmtp_2_2 = countMedTruePositives(2, 2, df_birads_phy, df_birads_real)
chtp_2_2 = countHghTruePositives(2, 2, df_birads_phy, df_birads_real)

cltp_3_3 = countLowTruePositives(3, 3, df_birads_phy, df_birads_real)
cmtp_3_3 = countMedTruePositives(3, 3, df_birads_phy, df_birads_real)
chtp_3_3 = countHghTruePositives(3, 3, df_birads_phy, df_birads_real)

cltp_4_4 = countLowTruePositives(4, 4, df_birads_phy, df_birads_real)
cmtp_4_4 = countMedTruePositives(4, 4, df_birads_phy, df_birads_real)
chtp_4_4 = countHghTruePositives(4, 4, df_birads_phy, df_birads_real)

cltp_5_5 = countLowTruePositives(5, 5, df_birads_phy, df_birads_real)
cmtp_5_5 = countMedTruePositives(5, 5, df_birads_phy, df_birads_real)
chtp_5_5 = countHghTruePositives(5, 5, df_birads_phy, df_birads_real)

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

# ============================== #
# ============================== #
#    COUNTING FALSE-POSITIVES    #
# ============================== #
# ============================== #

# ============================== #
#             Singles            #
# ============================== #

clfp_1_0 = countLowFalsePositives(1, 0, df_birads_phy, df_birads_real)
cmfp_1_0 = countMedFalsePositives(1, 0, df_birads_phy, df_birads_real)
chfp_1_0 = countHghFalsePositives(1, 0, df_birads_phy, df_birads_real)

clfp_2_0 = countLowFalsePositives(2, 0, df_birads_phy, df_birads_real)
cmfp_2_0 = countMedFalsePositives(2, 0, df_birads_phy, df_birads_real)
chfp_2_0 = countHghFalsePositives(2, 0, df_birads_phy, df_birads_real)

clfp_3_0 = countLowFalsePositives(3, 0, df_birads_phy, df_birads_real)
cmfp_3_0 = countMedFalsePositives(3, 0, df_birads_phy, df_birads_real)
chfp_3_0 = countHghFalsePositives(3, 0, df_birads_phy, df_birads_real)

clfp_4_0 = countLowFalsePositives(4, 0, df_birads_phy, df_birads_real)
cmfp_4_0 = countMedFalsePositives(4, 0, df_birads_phy, df_birads_real)
chfp_4_0 = countHghFalsePositives(4, 0, df_birads_phy, df_birads_real)

clfp_5_0 = countLowFalsePositives(5, 0, df_birads_phy, df_birads_real)
cmfp_5_0 = countMedFalsePositives(5, 0, df_birads_phy, df_birads_real)
chfp_5_0 = countHghFalsePositives(5, 0, df_birads_phy, df_birads_real)

clfp_2_1 = countLowFalsePositives(2, 1, df_birads_phy, df_birads_real)
cmfp_2_1 = countMedFalsePositives(2, 1, df_birads_phy, df_birads_real)
chfp_2_1 = countHghFalsePositives(2, 1, df_birads_phy, df_birads_real)

clfp_3_1 = countLowFalsePositives(3, 1, df_birads_phy, df_birads_real)
cmfp_3_1 = countMedFalsePositives(3, 1, df_birads_phy, df_birads_real)
chfp_3_1 = countHghFalsePositives(3, 1, df_birads_phy, df_birads_real)

clfp_4_1 = countLowFalsePositives(4, 1, df_birads_phy, df_birads_real)
cmfp_4_1 = countMedFalsePositives(4, 1, df_birads_phy, df_birads_real)
chfp_4_1 = countHghFalsePositives(4, 1, df_birads_phy, df_birads_real)

clfp_5_1 = countLowFalsePositives(5, 1, df_birads_phy, df_birads_real)
cmfp_5_1 = countMedFalsePositives(5, 1, df_birads_phy, df_birads_real)
chfp_5_1 = countHghFalsePositives(5, 1, df_birads_phy, df_birads_real)

clfp_3_2 = countLowFalsePositives(3, 2, df_birads_phy, df_birads_real)
cmfp_3_2 = countMedFalsePositives(3, 2, df_birads_phy, df_birads_real)
chfp_3_2 = countHghFalsePositives(3, 2, df_birads_phy, df_birads_real)

clfp_4_2 = countLowFalsePositives(4, 2, df_birads_phy, df_birads_real)
cmfp_4_2 = countMedFalsePositives(4, 2, df_birads_phy, df_birads_real)
chfp_4_2 = countHghFalsePositives(4, 2, df_birads_phy, df_birads_real)

clfp_5_2 = countLowFalsePositives(5, 2, df_birads_phy, df_birads_real)
cmfp_5_2 = countMedFalsePositives(5, 2, df_birads_phy, df_birads_real)
chfp_5_2 = countHghFalsePositives(5, 2, df_birads_phy, df_birads_real)

clfp_4_3 = countLowFalsePositives(4, 3, df_birads_phy, df_birads_real)
cmfp_4_3 = countMedFalsePositives(4, 3, df_birads_phy, df_birads_real)
chfp_4_3 = countHghFalsePositives(4, 3, df_birads_phy, df_birads_real)

clfp_5_3 = countLowFalsePositives(5, 3, df_birads_phy, df_birads_real)
cmfp_5_3 = countMedFalsePositives(5, 3, df_birads_phy, df_birads_real)
chfp_5_3 = countHghFalsePositives(5, 3, df_birads_phy, df_birads_real)

clfp_5_4 = countLowFalsePositives(5, 4, df_birads_phy, df_birads_real)
cmfp_5_4 = countMedFalsePositives(5, 4, df_birads_phy, df_birads_real)
chfp_5_4 = countHghFalsePositives(5, 4, df_birads_phy, df_birads_real)

# ============================== #

# ============================== #
#             Totals             #
# ============================== #

c_1_0 = clfp_1_0 + cmfp_1_0 + chfp_1_0
c_2_0 = clfp_2_0 + cmfp_2_0 + chfp_2_0
c_3_0 = clfp_3_0 + cmfp_3_0 + chfp_3_0
c_4_0 = clfp_4_0 + cmfp_4_0 + chfp_4_0
c_5_0 = clfp_5_0 + cmfp_5_0 + chfp_5_0

c_2_1 = clfp_2_1 + cmfp_2_1 + chfp_2_1
c_3_1 = clfp_3_1 + cmfp_3_1 + chfp_3_1
c_4_1 = clfp_4_1 + cmfp_4_1 + chfp_4_1
c_5_1 = clfp_5_1 + cmfp_5_1 + chfp_5_1

c_3_2 = clfp_3_2 + cmfp_3_2 + chfp_3_2
c_4_2 = clfp_4_2 + cmfp_4_2 + chfp_4_2
c_5_2 = clfp_5_2 + cmfp_5_2 + chfp_5_2

c_4_3 = clfp_4_3 + cmfp_4_3 + chfp_4_3
c_5_3 = clfp_5_3 + cmfp_5_3 + chfp_5_3

c_5_4 = clfp_5_4 + cmfp_5_4 + chfp_5_4

# ============================== #

# ============================== #
# ============================== #

# ============================== #
# ============================== #
#    COUNTING FALSE-NEGATIVES    #
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

c_2_2 = cltp_2_2 + cmtp_2_2 + chtp_2_2

c_2_3 = 1
c_2_4 = 1
c_2_5 = 1

c_3_0 = 1

c_3_3 = cltp_3_3 + cmtp_3_3 + chtp_3_3

c_3_4 = 1
c_3_5 = 1

c_4_0 = 1

c_4_4 = cltp_4_4 + cmtp_4_4 + chtp_4_4

c_4_5 = 1

c_5_0 = 1

c_5_5 = cltp_5_5 + cmtp_5_5 + chtp_5_5

# ==================== END File ==================== #