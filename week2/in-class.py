import pandas as pd

df = pd.read_csv('https://data.cdc.gov/api/views/hfr9-rurv/rows.csv?accessType=DOWNLOAD')

df.head(20)
# mask = df['Question'] == 'Percentage of older adults who are experiencing mental distress'
# question_df = df[mask]
# print(question_df)
# # question_df.shape() 

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid", color_codes=True)
plt.title('Percentage of older adults who are experiencing mental distress')

plot = sns.countplot(x='LocationDesc', color='b', data='')