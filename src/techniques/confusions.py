#!/usr/bin/env python
#coding=utf-8

"""
confusions.py: the presented file, serves the purpose of ploting our set
               of figures and respective heatmaps from techniques.
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

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.io as pio
import plotly.graph_objects as go

def confMatrixHeatmap(arrayCounters):
	logging.debug(arrayCounters)
	figConfMatrixHeatmap = plt.figure(figsize = (10,10))
	snsConfMatrixHeatmap = sns.heatmap(arrayCounters, annot = True, cbar = False)
	snsConfMatrixHeatmap.set(xlabel='Total Number of Actual BIRADS', ylabel='Total Number of Provided BIRADS')

def confMatrixHeatmapToHtml(arrayCounters, fileName):
	logging.debug(arrayCounters)
	figConfMatrixHeatmap = plt.figure(figsize = (10,10))
	snsConfMatrixHeatmap = sns.heatmap(arrayCounters, annot = True, cbar = False)
	snsConfMatrixHeatmap.set(xlabel='Total Number of Actual BIRADS', ylabel='Total Number of Provided BIRADS')
	plt.savefig(fileName)

# ==================== END File ==================== #