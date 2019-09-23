#!/usr/bin/env python
#coding=utf-8

"""
confusionTests.py: our purpose is to create a bunch of heatmaps for
                   our recall and precision probleam. For that, and
                   while we are using the same dataset, as always, we
                   want to test the resulted computation with static
                   values.
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
import unittest

from os import path

# The current folder path.
basePath = os.path.dirname(__file__)

# The path to the repository "src" folder.
joinRepoSrcPath = os.path.join(basePath, '..')
pathRepoSrcAbsPath = os.path.abspath(joinRepoSrcPath)
# Add the directory containing the module to
# the Python path (wants absolute paths).
sys.path.append(pathRepoSrcAbsPath)

# Appending structures path
strcPath = os.path.join(joinRepoSrcPath, 'structures')
strcAbsPath = os.path.abspath(strcPath)
sys.path.append(strcAbsPath)
sys.path.insert(0, strcAbsPath)

# Importing available structures
from counters import *

import numpy as np

class ConfusionMatrixTest(unittest.TestCase):
	# Classifications: Physician + Assistant vs Real
  def test_equal_conf_matrix_collab_real(self):
  	arrResult = acc001
  	arrToTest = np.array([[0,  3,  1,  0,  1,  0],
  		                    [0, 29,  2,  0,  0,  0],
  		                    [0, 12, 31,  4,  1,  0],
  		                    [0,  0,  4,  1,  3,  0],
  		                    [0,  1,  1,  1, 11,  4],
  		                    [0,  0,  0,  0,  1, 24]])
  	cond001 = np.array_equal(arrToTest, arrResult)
  	self.assertEqual(cond001, True)
  # Classifications: Physician vs Real
  def test_equal_conf_matrix_phys_real(self):
  	arrResult = acc002
  	arrToTest = np.array([[0,  9,  3,  0,  1,  3],
												  [0,  0,  0,  0,  1,  1],
												  [0, 13,  5,  1,  3,  5],
												  [0, 13,  5,  1,  2,  7],
												  [0,  8, 26,  4,  2,  2],
												  [0,  2,  0,  0,  8, 10]])
  	cond002 = np.array_equal(arrToTest, arrResult)
  	self.assertEqual(cond002, True)

if __name__ == "__main__":
  unittest.main()

# ==================== END File ==================== #