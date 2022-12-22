import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


def ex6(df: pd.DataFrame, value: float) -> pd.DataFrame:
    return df.loc[df['dev_mean'] >= value]
def index_change(df: pd.DataFrame) -> pd.DataFrame:
    test = df.shape[0]
    df.index = [i for i in range(0, int(test))]
    return df
def ex7(df: pd.DataFrame, data1: str, data2: str) -> pd.DataFrame:
    df= df.loc[(df['date'] >= data1) & (df['date'] <= data2)]
    return df


def main(path_to_csv: str=os.path.join("C:/", "Users", "79171", "PyCharmProjects", "lab4", "dataset.csv")) -> None:
    df = pd.read_csv(path_to_csv)
    print(df)
    df.columns = ['date', 'value']  
    print(df)
    nan_value = float("NaN")
    df.replace(" ", nan_value, inplace=True)
    df = df.dropna()

    df = index_change(df)
    print(df)
    df['dev_mean'] = df['value'].mean()-df['value']  # отклонение от среднего
    a=  (df.last_valid_index()+1)/2+0.5
    b = (df.last_valid_index()+1)/2-0.5
    print(a)
    print(df)

    df = index_change(df)
    print(df.dtypes)
    stats = df[['dev_mean']].describe()
    print(stats)

    value = 0.5 # 6
    df_1 = ex6(df, value)
    df_1= index_change(df_1)
    print(df_1)
    data1 = "2022-09-15"
    data2 = "2022-10-05"
    df_2 = ex7(df, data1, data2)
    df_2 = index_change(df_2)
    print(df_2)

main()
