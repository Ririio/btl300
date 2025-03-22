import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('assets/internetusage.csv')# load internetusage.csv 

population = df[['State', 'Population']]# subset the State and Population columns

state_index = int(input())

state_data = population.loc[[state_index]] # subset the row given by state_index
print(state_data)
state_name = state_data.iloc[0][0]

state_pop = state_data.iloc[0][1]

print("The population of " + str(state_name) + " is " + str(state_pop)+ ".")
sns.boxplot(data=population)
# create a box plot for the Population column using seaborn
plt.savefig("population_boxplot_python.png")