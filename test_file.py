import numpy as np
import pandas as pd

def get_uniques(list_test: list) -> np.array:
    return np.unique(list_test)

def sum_list(list_test: list) -> float:
    return np.sum(list_test)

def prod_list(list_test: list) -> float:
    return np.sum(list_test)

def calcular_promedios(df):
    return df.mean()

def calcular_tipos(df):
    print(df.dtypes)