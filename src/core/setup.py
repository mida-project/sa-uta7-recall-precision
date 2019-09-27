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


class VerifyVersionCommand(install):
  """Custom command to verify that the git tag matches our version"""
  description = 'verify that the git tag matches our version'

  def run(self):
    tag = os.getenv('CIRCLE_TAG')

    if tag != VERSION:
      info = "Git tag: {0} does not match the version of this app: {1}".format(
        tag, VERSION
      )
      sys.exit(info)

setup(
  name="sa-uta7-recall-precision",
  version=VERSION,
  description="Recall & Precision Problem UTA7 Statistical Analysis",
  long_description=readme(),
  url="https://github.com/mida-project/sa-uta7-recall-precision",
  author="Francisco Maria Calisto",
  author_email="francisco.calisto@tecnico.ulisboa.pt",
  license="MIT",
  classifiers=[
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "Intended Audience :: System Administrators",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Topic :: Software Development :: Build Tools",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Internet",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3 :: Only",
  ],
  keywords='circleci ci cd api sdk',
  packages=['circleci'],
  install_requires=[
    'requests==2.18.4',
  ],
  python_requires='>=3',
  cmdclass={
    'verify': VerifyVersionCommand,
  }
)

# ==================== END File ==================== #