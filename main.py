

import pandas as pd


df1 = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data")

df1.to_csv("autosCsv")

df1 = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")

df1.to_csv("Iris")
