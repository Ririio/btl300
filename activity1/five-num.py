import pandas as pd

df = pd.read_csv("assets/internetusage.csv")

internet = df[['internet_usage']] # subset the column internet_usage

five_num = internet.describe()# find the five number summary

print(five_num)