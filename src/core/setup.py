#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
setup.py: The file is the most important part of any Python
          package. It provides metadata for PyPI, handles all
          packaging tasks, and even allows you to add custom
          packaging-related commands.
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

from setuptools import setup
from setuptools.command.install import install

# sa-uta7-recall-precision version
VERSION = "1.0.0"

def readme():
  """print long description"""
  with open('README.md') as f:
    return f.read()

# ==================== END File ==================== #