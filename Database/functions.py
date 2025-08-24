import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# --------------
# Main functions
# --------------

# 1. Top-10 regions by harvested area, production and yield


def tops(df, cols):
    result = {}
    for col in cols:
        result[col] = df[['region', col]].sort_values(
            by=col, ascending=False
        ).head(10).copy()
    return result

# 2. Mean values of table


def mean_values(x):
    means = x[['harvested_area', 'volume_production',
               'yield_1ha']].mean().round(2).reset_index()
    means = means.rename(columns={'index': 'columns',  0: 'mean_values'})
    return means

# 3. Max values of table


def max_values(x):
    max = x[['harvested_area', 'volume_production',
             'yield_1ha']].max().reset_index()
    max = max.rename(columns={'index': 'columns',  0: 'max_values'})
    return max

# 3. Min values of table


def min_values(x):
    min = x[['harvested_area', 'volume_production',
             'yield_1ha']].min().reset_index()
    min = min.rename(columns={'index': 'columns',  0: 'max_values'})
    return min
