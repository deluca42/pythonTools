import pandas as pd 
import os 

def read_transform(path):
    df = pd.read_csv(path)
    colums = df.columns[:2]
    df = df[colums].dropna(how='any')
    df = df.set_index(["ano","uf"])
    return df

file_path = "deluca-ubuntu/all_files/"
filenames = os.listdir(file_path)

dfs = [read_transform(file_path+i) for i in filenames]

df_full =pd.concat(dfs, axis=l)
df_full.to_csv("deluca-ubuntu/all_files/consolidado.csv")
