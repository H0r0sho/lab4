import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os



def index_change(df: pd.DataFrame) -> pd.DataFrame:
    """updating indexes DataFrame"""
    test = df.shape[0]
    df.index = [i for i in range(0, int(test))]
    return df
