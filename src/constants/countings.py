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
# ============================== #
# ============================== #
#                                #
# Physician + Assistant vs Real  #
#                                #
# ============================== #
# ============================== #
# ============================== #
# ============================== #

# ============================== #
# ============================== #
#     COUNTING TRUE-POSITIVES    #
# ============================== #
# ============================== #

# ============================== #
#             Singles            #
# ============================== #

pltp_0_0 = countLow(0, 0, df_birads_phys, df_birads_real)
pmtp_0_0 = countMed(0, 0, df_birads_phys, df_birads_real)
phtp_0_0 = countHgh(0, 0, df_birads_phys, df_birads_real)

pltp_1_1 = countLow(1, 1, df_birads_phys, df_birads_real)
pmtp_1_1 = countMed(1, 1, df_birads_phys, df_birads_real)
phtp_1_1 = countHgh(1, 1, df_birads_phys, df_birads_real)

pltp_2_2 = countLow(2, 2, df_birads_phys, df_birads_real)
pmtp_2_2 = countMed(2, 2, df_birads_phys, df_birads_real)
phtp_2_2 = countHgh(2, 2, df_birads_phys, df_birads_real)

pltp_3_3 = countLow(3, 3, df_birads_phys, df_birads_real)
pmtp_3_3 = countMed(3, 3, df_birads_phys, df_birads_real)
phtp_3_3 = countHgh(3, 3, df_birads_phys, df_birads_real)

pltp_4_4 = countLow(4, 4, df_birads_phys, df_birads_real)
pmtp_4_4 = countMed(4, 4, df_birads_phys, df_birads_real)
phtp_4_4 = countHgh(4, 4, df_birads_phys, df_birads_real)

pltp_5_5 = countLow(5, 5, df_birads_phys, df_birads_real)
pmtp_5_5 = countMed(5, 5, df_birads_phys, df_birads_real)
phtp_5_5 = countHgh(5, 5, df_birads_phys, df_birads_real)

# ============================== #

# ============================== #
#             Totals             #
# ============================== #

c_0_0 = pltp_0_0 + pmtp_0_0 + phtp_0_0
c_1_1 = pltp_1_1 + pmtp_1_1 + phtp_1_1
c_2_2 = pltp_2_2 + pmtp_2_2 + phtp_2_2
c_3_3 = pltp_3_3 + pmtp_3_3 + phtp_3_3
c_4_4 = pltp_4_4 + pmtp_4_4 + phtp_4_4
c_5_5 = pltp_5_5 + pmtp_5_5 + phtp_5_5

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

clfp_1_0 = countLow(1, 0, df_birads_phys, df_birads_real)
cmfp_1_0 = countMed(1, 0, df_birads_phys, df_birads_real)
chfp_1_0 = countHgh(1, 0, df_birads_phys, df_birads_real)

clfp_2_0 = countLow(2, 0, df_birads_phys, df_birads_real)
cmfp_2_0 = countMed(2, 0, df_birads_phys, df_birads_real)
chfp_2_0 = countHgh(2, 0, df_birads_phys, df_birads_real)

clfp_3_0 = countLow(3, 0, df_birads_phys, df_birads_real)
cmfp_3_0 = countMed(3, 0, df_birads_phys, df_birads_real)
chfp_3_0 = countHgh(3, 0, df_birads_phys, df_birads_real)

clfp_4_0 = countLow(4, 0, df_birads_phys, df_birads_real)
cmfp_4_0 = countMed(4, 0, df_birads_phys, df_birads_real)
chfp_4_0 = countHgh(4, 0, df_birads_phys, df_birads_real)

clfp_5_0 = countLow(5, 0, df_birads_phys, df_birads_real)
cmfp_5_0 = countMed(5, 0, df_birads_phys, df_birads_real)
chfp_5_0 = countHgh(5, 0, df_birads_phys, df_birads_real)

clfp_2_1 = countLow(2, 1, df_birads_phys, df_birads_real)
cmfp_2_1 = countMed(2, 1, df_birads_phys, df_birads_real)
chfp_2_1 = countHgh(2, 1, df_birads_phys, df_birads_real)

clfp_3_1 = countLow(3, 1, df_birads_phys, df_birads_real)
cmfp_3_1 = countMed(3, 1, df_birads_phys, df_birads_real)
chfp_3_1 = countHgh(3, 1, df_birads_phys, df_birads_real)

clfp_4_1 = countLow(4, 1, df_birads_phys, df_birads_real)
cmfp_4_1 = countMed(4, 1, df_birads_phys, df_birads_real)
chfp_4_1 = countHgh(4, 1, df_birads_phys, df_birads_real)

clfp_5_1 = countLow(5, 1, df_birads_phys, df_birads_real)
cmfp_5_1 = countMed(5, 1, df_birads_phys, df_birads_real)
chfp_5_1 = countHgh(5, 1, df_birads_phys, df_birads_real)

clfp_3_2 = countLow(3, 2, df_birads_phys, df_birads_real)
cmfp_3_2 = countMed(3, 2, df_birads_phys, df_birads_real)
chfp_3_2 = countHgh(3, 2, df_birads_phys, df_birads_real)

clfp_4_2 = countLow(4, 2, df_birads_phys, df_birads_real)
cmfp_4_2 = countMed(4, 2, df_birads_phys, df_birads_real)
chfp_4_2 = countHgh(4, 2, df_birads_phys, df_birads_real)

clfp_5_2 = countLow(5, 2, df_birads_phys, df_birads_real)
cmfp_5_2 = countMed(5, 2, df_birads_phys, df_birads_real)
chfp_5_2 = countHgh(5, 2, df_birads_phys, df_birads_real)

clfp_4_3 = countLow(4, 3, df_birads_phys, df_birads_real)
cmfp_4_3 = countMed(4, 3, df_birads_phys, df_birads_real)
chfp_4_3 = countHgh(4, 3, df_birads_phys, df_birads_real)

clfp_5_3 = countLow(5, 3, df_birads_phys, df_birads_real)
cmfp_5_3 = countMed(5, 3, df_birads_phys, df_birads_real)
chfp_5_3 = countHgh(5, 3, df_birads_phys, df_birads_real)

clfp_5_4 = countLow(5, 4, df_birads_phys, df_birads_real)
cmfp_5_4 = countMed(5, 4, df_birads_phys, df_birads_real)
chfp_5_4 = countHgh(5, 4, df_birads_phys, df_birads_real)

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

clfn_0_1 = countLow(0, 1, df_birads_phys, df_birads_real)
cmfn_0_1 = countMed(0, 1, df_birads_phys, df_birads_real)
chfn_0_1 = countHgh(0, 1, df_birads_phys, df_birads_real)

clfn_0_2 = countLow(0, 2, df_birads_phys, df_birads_real)
cmfn_0_2 = countMed(0, 2, df_birads_phys, df_birads_real)
chfn_0_2 = countHgh(0, 2, df_birads_phys, df_birads_real)

clfn_0_3 = countLow(0, 3, df_birads_phys, df_birads_real)
cmfn_0_3 = countMed(0, 3, df_birads_phys, df_birads_real)
chfn_0_3 = countHgh(0, 3, df_birads_phys, df_birads_real)

clfn_0_4 = countLow(0, 4, df_birads_phys, df_birads_real)
cmfn_0_4 = countMed(0, 4, df_birads_phys, df_birads_real)
chfn_0_4 = countHgh(0, 4, df_birads_phys, df_birads_real)

clfn_0_5 = countLow(0, 5, df_birads_phys, df_birads_real)
cmfn_0_5 = countMed(0, 5, df_birads_phys, df_birads_real)
chfn_0_5 = countHgh(0, 5, df_birads_phys, df_birads_real)

clfn_1_2 = countLow(1, 2, df_birads_phys, df_birads_real)
cmfn_1_2 = countMed(1, 2, df_birads_phys, df_birads_real)
chfn_1_2 = countHgh(1, 2, df_birads_phys, df_birads_real)

clfn_1_3 = countLow(1, 3, df_birads_phys, df_birads_real)
cmfn_1_3 = countMed(1, 3, df_birads_phys, df_birads_real)
chfn_1_3 = countHgh(1, 3, df_birads_phys, df_birads_real)

clfn_1_4 = countLow(1, 4, df_birads_phys, df_birads_real)
cmfn_1_4 = countMed(1, 4, df_birads_phys, df_birads_real)
chfn_1_4 = countHgh(1, 4, df_birads_phys, df_birads_real)

clfn_1_5 = countLow(1, 5, df_birads_phys, df_birads_real)
cmfn_1_5 = countMed(1, 5, df_birads_phys, df_birads_real)
chfn_1_5 = countHgh(1, 5, df_birads_phys, df_birads_real)

clfn_2_3 = countLow(2, 3, df_birads_phys, df_birads_real)
cmfn_2_3 = countMed(2, 3, df_birads_phys, df_birads_real)
chfn_2_3 = countHgh(2, 3, df_birads_phys, df_birads_real)

clfn_2_4 = countLow(2, 4, df_birads_phys, df_birads_real)
cmfn_2_4 = countMed(2, 4, df_birads_phys, df_birads_real)
chfn_2_4 = countHgh(2, 4, df_birads_phys, df_birads_real)

clfn_2_5 = countLow(2, 5, df_birads_phys, df_birads_real)
cmfn_2_5 = countMed(2, 5, df_birads_phys, df_birads_real)
chfn_2_5 = countHgh(2, 5, df_birads_phys, df_birads_real)

clfn_3_4 = countLow(3, 4, df_birads_phys, df_birads_real)
cmfn_3_4 = countMed(3, 4, df_birads_phys, df_birads_real)
chfn_3_4 = countHgh(3, 4, df_birads_phys, df_birads_real)

clfn_3_5 = countLow(3, 5, df_birads_phys, df_birads_real)
cmfn_3_5 = countMed(3, 5, df_birads_phys, df_birads_real)
chfn_3_5 = countHgh(3, 5, df_birads_phys, df_birads_real)

clfn_4_5 = countLow(4, 5, df_birads_phys, df_birads_real)
cmfn_4_5 = countMed(4, 5, df_birads_phys, df_birads_real)
chfn_4_5 = countHgh(4, 5, df_birads_phys, df_birads_real)

# ============================== #

# ============================== #
#             Totals             #
# ============================== #

# ============================== #

c_0_1 = clfn_0_1 + cmfn_0_1 + chfn_0_1
c_0_2 = clfn_0_2 + cmfn_0_2 + chfn_0_2
c_0_3 = clfn_0_3 + cmfn_0_3 + chfn_0_3
c_0_4 = clfn_0_4 + cmfn_0_4 + chfn_0_4
c_0_5 = clfn_0_5 + cmfn_0_5 + chfn_0_5

c_1_2 = clfn_1_2 + cmfn_1_2 + chfn_1_2
c_1_3 = clfn_1_3 + cmfn_1_3 + chfn_1_3
c_1_4 = clfn_1_4 + cmfn_1_4 + chfn_1_4
c_1_5 = clfn_1_5 + cmfn_1_5 + chfn_1_5

c_2_3 = clfn_2_3 + cmfn_2_3 + chfn_2_3
c_2_4 = clfn_2_4 + cmfn_2_4 + chfn_2_4
c_2_5 = clfn_2_5 + cmfn_2_5 + chfn_2_5

c_3_4 = clfn_3_4 + cmfn_3_4 + chfn_3_4
c_3_5 = clfn_3_5 + cmfn_3_5 + chfn_3_5

c_4_5 = clfn_4_5 + cmfn_4_5 + chfn_4_5

# ============================== #
# ============================== #
# ============================== #
# ============================== #

# ============================== #
# ============================== #
# ============================== #
# ============================== #
#                                #
#       Physician vs Real        #
#                                #
# ============================== #
# ============================== #
# ============================== #
# ============================== #


# ============================== #
# ============================== #
#     COUNTING TRUE-POSITIVES    #
# ============================== #
# ============================== #

# ============================== #
#             Singles            #
# ============================== #

pltp_0_0 = countLow(0, 0, df_birads_crrnt, df_birads_real)
pmtp_0_0 = countMed(0, 0, df_birads_crrnt, df_birads_real)
phtp_0_0 = countHgh(0, 0, df_birads_crrnt, df_birads_real)

pltp_1_1 = countLow(1, 1, df_birads_crrnt, df_birads_real)
pmtp_1_1 = countMed(1, 1, df_birads_crrnt, df_birads_real)
phtp_1_1 = countHgh(1, 1, df_birads_crrnt, df_birads_real)

pltp_2_2 = countLow(2, 2, df_birads_crrnt, df_birads_real)
pmtp_2_2 = countMed(2, 2, df_birads_crrnt, df_birads_real)
phtp_2_2 = countHgh(2, 2, df_birads_crrnt, df_birads_real)

pltp_3_3 = countLow(3, 3, df_birads_crrnt, df_birads_real)
pmtp_3_3 = countMed(3, 3, df_birads_crrnt, df_birads_real)
phtp_3_3 = countHgh(3, 3, df_birads_crrnt, df_birads_real)

pltp_4_4 = countLow(4, 4, df_birads_crrnt, df_birads_real)
pmtp_4_4 = countMed(4, 4, df_birads_crrnt, df_birads_real)
phtp_4_4 = countHgh(4, 4, df_birads_crrnt, df_birads_real)

pltp_5_5 = countLow(5, 5, df_birads_crrnt, df_birads_real)
pmtp_5_5 = countMed(5, 5, df_birads_crrnt, df_birads_real)
phtp_5_5 = countHgh(5, 5, df_birads_crrnt, df_birads_real)

# ============================== #

# ============================== #
#             Totals             #
# ============================== #

p_0_0 = pltp_0_0 + pmtp_0_0 + phtp_0_0
p_1_1 = pltp_1_1 + pmtp_1_1 + phtp_1_1
p_2_2 = pltp_2_2 + pmtp_2_2 + phtp_2_2
p_3_3 = pltp_3_3 + pmtp_3_3 + phtp_3_3
p_4_4 = pltp_4_4 + pmtp_4_4 + phtp_4_4
p_5_5 = pltp_5_5 + pmtp_5_5 + phtp_5_5

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

plfp_1_0 = countLow(1, 0, df_birads_crrnt, df_birads_real)
pmfp_1_0 = countMed(1, 0, df_birads_crrnt, df_birads_real)
phfp_1_0 = countHgh(1, 0, df_birads_crrnt, df_birads_real)

plfp_2_0 = countLow(2, 0, df_birads_crrnt, df_birads_real)
pmfp_2_0 = countMed(2, 0, df_birads_crrnt, df_birads_real)
phfp_2_0 = countHgh(2, 0, df_birads_crrnt, df_birads_real)

plfp_3_0 = countLow(3, 0, df_birads_crrnt, df_birads_real)
pmfp_3_0 = countMed(3, 0, df_birads_crrnt, df_birads_real)
phfp_3_0 = countHgh(3, 0, df_birads_crrnt, df_birads_real)

plfp_4_0 = countLow(4, 0, df_birads_crrnt, df_birads_real)
pmfp_4_0 = countMed(4, 0, df_birads_crrnt, df_birads_real)
phfp_4_0 = countHgh(4, 0, df_birads_crrnt, df_birads_real)

plfp_5_0 = countLow(5, 0, df_birads_crrnt, df_birads_real)
pmfp_5_0 = countMed(5, 0, df_birads_crrnt, df_birads_real)
phfp_5_0 = countHgh(5, 0, df_birads_crrnt, df_birads_real)

plfp_2_1 = countLow(2, 1, df_birads_crrnt, df_birads_real)
pmfp_2_1 = countMed(2, 1, df_birads_crrnt, df_birads_real)
phfp_2_1 = countHgh(2, 1, df_birads_crrnt, df_birads_real)

plfp_3_1 = countLow(3, 1, df_birads_crrnt, df_birads_real)
pmfp_3_1 = countMed(3, 1, df_birads_crrnt, df_birads_real)
phfp_3_1 = countHgh(3, 1, df_birads_crrnt, df_birads_real)

plfp_4_1 = countLow(4, 1, df_birads_crrnt, df_birads_real)
pmfp_4_1 = countMed(4, 1, df_birads_crrnt, df_birads_real)
phfp_4_1 = countHgh(4, 1, df_birads_crrnt, df_birads_real)

plfp_5_1 = countLow(5, 1, df_birads_crrnt, df_birads_real)
pmfp_5_1 = countMed(5, 1, df_birads_crrnt, df_birads_real)
phfp_5_1 = countHgh(5, 1, df_birads_crrnt, df_birads_real)

plfp_3_2 = countLow(3, 2, df_birads_crrnt, df_birads_real)
pmfp_3_2 = countMed(3, 2, df_birads_crrnt, df_birads_real)
phfp_3_2 = countHgh(3, 2, df_birads_crrnt, df_birads_real)

plfp_4_2 = countLow(4, 2, df_birads_crrnt, df_birads_real)
pmfp_4_2 = countMed(4, 2, df_birads_crrnt, df_birads_real)
phfp_4_2 = countHgh(4, 2, df_birads_crrnt, df_birads_real)

plfp_5_2 = countLow(5, 2, df_birads_crrnt, df_birads_real)
pmfp_5_2 = countMed(5, 2, df_birads_crrnt, df_birads_real)
phfp_5_2 = countHgh(5, 2, df_birads_crrnt, df_birads_real)

plfp_4_3 = countLow(4, 3, df_birads_crrnt, df_birads_real)
pmfp_4_3 = countMed(4, 3, df_birads_crrnt, df_birads_real)
phfp_4_3 = countHgh(4, 3, df_birads_crrnt, df_birads_real)

plfp_5_3 = countLow(5, 3, df_birads_crrnt, df_birads_real)
pmfp_5_3 = countMed(5, 3, df_birads_crrnt, df_birads_real)
phfp_5_3 = countHgh(5, 3, df_birads_crrnt, df_birads_real)

plfp_5_4 = countLow(5, 4, df_birads_crrnt, df_birads_real)
pmfp_5_4 = countMed(5, 4, df_birads_crrnt, df_birads_real)
phfp_5_4 = countHgh(5, 4, df_birads_crrnt, df_birads_real)

# ============================== #

# ============================== #
#             Totals             #
# ============================== #

p_1_0 = plfp_1_0 + pmfp_1_0 + phfp_1_0
p_2_0 = plfp_2_0 + pmfp_2_0 + phfp_2_0
p_3_0 = plfp_3_0 + pmfp_3_0 + phfp_3_0
p_4_0 = plfp_4_0 + pmfp_4_0 + phfp_4_0
p_5_0 = plfp_5_0 + pmfp_5_0 + phfp_5_0

p_2_1 = plfp_2_1 + pmfp_2_1 + phfp_2_1
p_3_1 = plfp_3_1 + pmfp_3_1 + phfp_3_1
p_4_1 = plfp_4_1 + pmfp_4_1 + phfp_4_1
p_5_1 = plfp_5_1 + pmfp_5_1 + phfp_5_1

p_3_2 = plfp_3_2 + pmfp_3_2 + phfp_3_2
p_4_2 = plfp_4_2 + pmfp_4_2 + phfp_4_2
p_5_2 = plfp_5_2 + pmfp_5_2 + phfp_5_2

p_4_3 = plfp_4_3 + pmfp_4_3 + phfp_4_3
p_5_3 = plfp_5_3 + pmfp_5_3 + phfp_5_3

p_5_4 = plfp_5_4 + pmfp_5_4 + phfp_5_4

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

plfn_0_1 = countLow(0, 1, df_birads_crrnt, df_birads_real)
pmfn_0_1 = countMed(0, 1, df_birads_crrnt, df_birads_real)
phfn_0_1 = countHgh(0, 1, df_birads_crrnt, df_birads_real)

plfn_0_2 = countLow(0, 2, df_birads_crrnt, df_birads_real)
pmfn_0_2 = countMed(0, 2, df_birads_crrnt, df_birads_real)
phfn_0_2 = countHgh(0, 2, df_birads_crrnt, df_birads_real)

plfn_0_3 = countLow(0, 3, df_birads_crrnt, df_birads_real)
pmfn_0_3 = countMed(0, 3, df_birads_crrnt, df_birads_real)
phfn_0_3 = countHgh(0, 3, df_birads_crrnt, df_birads_real)

plfn_0_4 = countLow(0, 4, df_birads_crrnt, df_birads_real)
pmfn_0_4 = countMed(0, 4, df_birads_crrnt, df_birads_real)
phfn_0_4 = countHgh(0, 4, df_birads_crrnt, df_birads_real)

plfn_0_5 = countLow(0, 5, df_birads_crrnt, df_birads_real)
pmfn_0_5 = countMed(0, 5, df_birads_crrnt, df_birads_real)
phfn_0_5 = countHgh(0, 5, df_birads_crrnt, df_birads_real)

plfn_1_2 = countLow(1, 2, df_birads_crrnt, df_birads_real)
pmfn_1_2 = countMed(1, 2, df_birads_crrnt, df_birads_real)
phfn_1_2 = countHgh(1, 2, df_birads_crrnt, df_birads_real)

plfn_1_3 = countLow(1, 3, df_birads_crrnt, df_birads_real)
pmfn_1_3 = countMed(1, 3, df_birads_crrnt, df_birads_real)
phfn_1_3 = countHgh(1, 3, df_birads_crrnt, df_birads_real)

plfn_1_4 = countLow(1, 4, df_birads_crrnt, df_birads_real)
pmfn_1_4 = countMed(1, 4, df_birads_crrnt, df_birads_real)
phfn_1_4 = countHgh(1, 4, df_birads_crrnt, df_birads_real)

plfn_1_5 = countLow(1, 5, df_birads_crrnt, df_birads_real)
pmfn_1_5 = countMed(1, 5, df_birads_crrnt, df_birads_real)
phfn_1_5 = countHgh(1, 5, df_birads_crrnt, df_birads_real)

plfn_2_3 = countLow(2, 3, df_birads_crrnt, df_birads_real)
pmfn_2_3 = countMed(2, 3, df_birads_crrnt, df_birads_real)
phfn_2_3 = countHgh(2, 3, df_birads_crrnt, df_birads_real)

plfn_2_4 = countLow(2, 4, df_birads_crrnt, df_birads_real)
pmfn_2_4 = countMed(2, 4, df_birads_crrnt, df_birads_real)
phfn_2_4 = countHgh(2, 4, df_birads_crrnt, df_birads_real)

plfn_2_5 = countLow(2, 5, df_birads_crrnt, df_birads_real)
pmfn_2_5 = countMed(2, 5, df_birads_crrnt, df_birads_real)
phfn_2_5 = countHgh(2, 5, df_birads_crrnt, df_birads_real)

plfn_3_4 = countLow(3, 4, df_birads_crrnt, df_birads_real)
pmfn_3_4 = countMed(3, 4, df_birads_crrnt, df_birads_real)
phfn_3_4 = countHgh(3, 4, df_birads_crrnt, df_birads_real)

plfn_3_5 = countLow(3, 5, df_birads_crrnt, df_birads_real)
pmfn_3_5 = countMed(3, 5, df_birads_crrnt, df_birads_real)
phfn_3_5 = countHgh(3, 5, df_birads_crrnt, df_birads_real)

plfn_4_5 = countLow(4, 5, df_birads_crrnt, df_birads_real)
pmfn_4_5 = countMed(4, 5, df_birads_crrnt, df_birads_real)
phfn_4_5 = countHgh(4, 5, df_birads_crrnt, df_birads_real)

# ============================== #

# ============================== #
#             Totals             #
# ============================== #

# ============================== #

p_0_1 = plfn_0_1 + pmfn_0_1 + phfn_0_1
p_0_2 = plfn_0_2 + pmfn_0_2 + phfn_0_2
p_0_3 = plfn_0_3 + pmfn_0_3 + phfn_0_3
p_0_4 = plfn_0_4 + pmfn_0_4 + phfn_0_4
p_0_5 = plfn_0_5 + pmfn_0_5 + phfn_0_5

p_1_2 = plfn_1_2 + pmfn_1_2 + phfn_1_2
p_1_3 = plfn_1_3 + pmfn_1_3 + phfn_1_3
p_1_4 = plfn_1_4 + pmfn_1_4 + phfn_1_4
p_1_5 = plfn_1_5 + pmfn_1_5 + phfn_1_5

p_2_3 = plfn_2_3 + pmfn_2_3 + phfn_2_3
p_2_4 = plfn_2_4 + pmfn_2_4 + phfn_2_4
p_2_5 = plfn_2_5 + pmfn_2_5 + phfn_2_5

p_3_4 = plfn_3_4 + pmfn_3_4 + phfn_3_4
p_3_5 = plfn_3_5 + pmfn_3_5 + phfn_3_5

p_4_5 = plfn_4_5 + pmfn_4_5 + phfn_4_5

# ============================== #
# ============================== #
# ============================== #
# ============================== #

# ==================== END File ==================== #