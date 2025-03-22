import pandas as pd


cars_df = pd.read_csv("Cars.csv")

userNum = int(input())

subset = cars_df[["Quality", "Speed", "Angle"]].head(userNum).max()

# Subset the first userNum rows of the data frame

print(subset)
