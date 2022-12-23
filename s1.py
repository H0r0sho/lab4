import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

def ex10(df: pd.DataFrame, year: int, month: int) -> pd.DataFrame:
    if (month < 10): month = "0" + str(month)
    datemin = str(str(year) + "-" + str(month) + "-" + "01")
    datemax = str(str(year) + "-" + str(month) + "-" + "31")
    df_sorted = df.loc[(df['date'] >= datemin) & (df['date'] <= datemax)]
    df_sorted = index_change(df_sorted)

    fig = plt.figure(figsize=(10, 5))
    plt.title("Value by month")  # Fahrenheit temperature graph
    plt.xlabel("Day")
    plt.ylabel("Value")
    plt.plot(df_sorted['value'], color="#ffa4fa", linestyle="--", marker="x", linewidth=1, markersize=6)
    plt.axhline(y=(df_sorted["value"]).mean(), color="#fe0df3", linewidth=1)
    plt.axhline(y=np.median(df_sorted["value"]), color="#592056", linestyle="-", linewidth=1)
    plt.legend(["Value in current day", "average", "median"])
    plt.show()
def ex6(df: pd.DataFrame, value: float) -> pd.DataFrame:
    return df.loc[df['dev_mean'] >= value]
def index_change(df: pd.DataFrame) -> pd.DataFrame:
    test = df.shape[0]
    df.index = [i for i in range(0, int(test))]
    return df
def ex7(df: pd.DataFrame, data1: str, data2: str) -> pd.DataFrame:
    df= df.loc[(df['date'] >= data1) & (df['date'] <= data2)]
    return df
def sort_by_month(df: pd.DataFrame, year: int, month: int) -> pd.DataFrame:
    if (month < 10): month = "0" + str(month)
    datemin = str(str(year) + "-" + str(month) + "-" + "01")
    datemax = str(str(year) + "-" + str(month) + "-" + "31")
    df_sorted = df.loc[(df['date'] >= datemin) & (df['date'] <= datemax)]
    df_sorted = index_change(df_sorted)
    return(df_sorted)
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
    df['dev_mean'] = df['value'].mean()-df['value']
    df['dev_med']=np.median(df["value"])-df['value']
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
    month, year = 10, 2022
    sort_by_month(df, year, month)
    df_3=sort_by_month(df, year, month)
    df_3_avg=df_3['value'].mean()
    print(df_3)
    print(df_3_avg)
    df = index_change(df)

    fig = plt.figure(figsize=(10, 5))
    ax = fig.add_subplot(211)
    ax.plot(df['value'], color="#fe0df3")
    plt.legend(["Value in current day"])
    plt.xlabel("Day")
    plt.ylabel("Value")
    plt.show()
    ex10(df, year, month)

main()
