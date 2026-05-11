import numpy as np

def compute_average(values):
    if len(values) == 0:
        return 0
    return np.mean(values)

def compute_median(values):
    if len(values) == 0:
        return 0
    return np.median(values)

def compute_standard_deviation(values):
    if len(values) == 0:
        return 0
    return np.std(values)

def compute_variance(values):
    if len(values) == 0:
        return 0
    return np.var(values)

def compute_maximum(values):
    if len(values) == 0:
        return 0
    return np.max(values)

def compute_minimum(values):
    if len(values) == 0:
        return 0
    return np.min(values)

def newest_camera(df):
    if df.empty:
        return None
    newest=df.loc[df["Release date"].idxmax()]
    return newest["Model"], newest["Release date"]

def expensive_camera(df,threshold):
    if df.empty:
        return None
    expensive=df.loc[df["Price"]>threshold]
    return expensive