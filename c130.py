import pandas as pd
import csv
reading=pd.read_csv('final_stars.csv')
reading=reading.dropna()
del reading["Unnamed: 0"]
del reading["Unnamed: 0.1"]
print(reading.shape)
print(reading.head())
reading.to_csv("cleaned_final_stars.csv",index=False)

