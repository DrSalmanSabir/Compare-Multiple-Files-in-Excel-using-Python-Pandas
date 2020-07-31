import pandas as pd
import numpy as np

def compareData(input1, input2):
    df1, df2 = pd.read_excel(input1), pd.read_excel(input2)
    # ON is the id in both files and HOW = inner is exact match
    df3 = pd.merge(df1, df2, on = 'account id', how = 'inner')
    # deleting the columns whose all values are nan
    df4 = df3.dropna(axis=1,how='all')
    # renaming the column of user id
    finalData = df4.rename(columns={'user id_y':'user id'})
    # To rename multiple columns use the following
    # newData = finalData.columns('Account ID', 'Age', 'User ID', 'Name')
    # To drop Table
    return finalData

compareData("File1.xlsx", "File2.xlsx")
