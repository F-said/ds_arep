import pandas as pd


def test1(result1):
    data = pd.read_csv("data/modify_test.csv")

    return data.equals(result1)