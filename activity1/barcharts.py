import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

titanic = pd.read_csv("assets/titanic.csv")

first_south = titanic[
    (titanic["pclass"] == 1) & (titanic["embarked"] == "S")
]  # subset the titanic dataset to include first class passengers who embarked in Southampton

second_third = titanic[
    titanic["pclass"].isin([2, 3])
]  # subset the titanic dataset to include either second or third class passengers

print(first_south.head())
print(second_third.head())

# Set the style of the bar charts
sns.set_theme(style="whitegrid", color_codes=True)

# Create a bar chart for the first class passengers who embarked in Southampton grouped by sex
# Your code here
sns.countplot(x="pclass", hue="sex", data=first_south)
# plt.savefig("bar_1.png")
plt.show()

# Create a bar chart for the second and third class passengers grouped by survival status
# Your code here
plt.legend(labels=["0", "1"], title="survived")
sns.countplot(x="pclass", hue="survived", data=second_third)
# plt.savefig("bar_2.png")
plt.show()
