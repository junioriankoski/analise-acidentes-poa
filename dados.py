import pandas as pd

df = pd.read_csv("cat_acidentes.csv", sep=";")
df_tratado = df.copy()