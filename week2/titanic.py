# import seaborn as sns

# titanic = sns.load_dataset('titanic')
# # print(f"Number of rows: {titanic.shape[0]}")
# # print(f"Column names: {[column for column in titanic.columns]}")
# # print(f"Data Types: {titanic.dtypes}")

import pandas as pd

titanic = pd.read_csv('titanic.csv')

print(f"Number of rows: {titanic.shape[0]}")