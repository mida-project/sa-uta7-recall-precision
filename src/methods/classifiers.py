#!/usr/bin/env python
#coding=utf-8

"""
classifiers.py: the classifiers file gives a complete picture of
                how the classifier is performing. It also allows
                to compute various classification metrics, while
                these metrics can guide our model selection.
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

from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

def classConfusionMatrix(df_real, df_pred):
	var_confusion_matrix = confusion_matrix(df_real, df_pred)
	return var_confusion_matrix

def classReport(df_real, df_pred):
	var_classification_report = classification_report(df_real, df_pred)
	return var_classification_report

# ==================== END File ==================== #