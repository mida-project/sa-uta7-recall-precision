#!/usr/bin/env python
#coding=utf-8

"""
precisionHeatmaps.py:
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

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.io as pio

def precHeatmap(arrayCounters):
	print(arrayCounters)
	figPrecHeatmap = plt.figure(figsize = (10,10))
	snsPrecHeatmap = sns.heatmap(arrayCounters, annot = True, cbar = False)

# ==================== END File ==================== #