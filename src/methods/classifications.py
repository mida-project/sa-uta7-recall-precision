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

# ============================== #
# ============================== #
#     COUNTING TRUE-NEGATIVES    #
# ============================== #
# ============================== #

def countLowTruePositives(val_collab, val_real, df_collab, df_real):
	aux_count = 0
	for i in range(len(df_real)):
		comp_collab = df_collab.iloc[i].low
		comp_real = df_real.iloc[i].low
		cond001 = val_collab == val_real == comp_collab == comp_real
		if cond001:
			aux_count += 1
	return aux_count

def countMedTruePositives(val_collab, val_real, df_collab, df_real):
	aux_count = 0
	for i in range(len(df_real)):
		comp_collab = df_collab.iloc[i].medium
		comp_real = df_real.iloc[i].medium
		cond001 = val_collab == val_real == comp_collab == comp_real
		if cond001:
			aux_count += 1
	return aux_count

def countHghTruePositives(val_collab, val_real, df_collab, df_real):
	aux_count = 0
	for i in range(len(df_real)):
		comp_collab = df_collab.iloc[i].high
		comp_real = df_real.iloc[i].high
		cond001 = val_collab == val_real == comp_collab == comp_real
		if cond001:
			aux_count += 1
	return aux_count

# ============================== #
# ============================== #

# ============================== #
# ============================== #
#     COUNTING TRUE-POSITIVES    #
# ============================== #
# ============================== #

# ============================== #
# ============================== #

# ============================== #
# ============================== #
#    COUNTING FALSE-POSITIVES    #
# ============================== #
# ============================== #

def countLowFalsePositives(val_collab, val_real, df_collab, df_real):
	aux_count = 0
	for i in range(len(df_real)):
		comp_collab = df_collab.iloc[i].low
		comp_real = df_real.iloc[i].low
		cond001 = val_collab == comp_collab
		cond002 = val_real == comp_real
		if cond001 and cond002:
			aux_count += 1
	return aux_count

def countMedFalsePositives(val_collab, val_real, df_collab, df_real):
	aux_count = 0
	for i in range(len(df_real)):
		comp_collab = df_collab.iloc[i].medium
		comp_real = df_real.iloc[i].medium
		cond001 = val_collab == comp_collab
		cond002 = val_real == comp_real
		if cond001 and cond002:
			aux_count += 1
	return aux_count

def countHghFalsePositives(val_collab, val_real, df_collab, df_real):
	aux_count = 0
	for i in range(len(df_real)):
		comp_collab = df_collab.iloc[i].high
		comp_real = df_real.iloc[i].high
		cond001 = val_collab == comp_collab
		cond002 = val_real == comp_real
		if cond001 and cond002:
			aux_count += 1
	return aux_count

# ============================== #
# ============================== #

# ============================== #
# ============================== #
#    COUNTING FALSE-NEGATIVES    #
# ============================== #
# ============================== #

# ============================== #
# ============================== #

# ==================== END File ==================== #