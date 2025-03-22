import pandas as pd

cylinders = int(input())

df = pd.read_csv("./assets/mtcars.csv")

df_cyl = df[df["cyl"] == cylinders]

# print the shape of the new data frame)
print(df_cyl.shape)
