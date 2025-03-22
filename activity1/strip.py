import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

titanic = pd.read_csv("assets/titanic.csv")  # load the titanic.csv dataset

df = titanic[
    (titanic["pclass"] == 1) & (titanic["sex"] == "male") & (titanic["age"] > 18)
]  # subset titanic to include male passengers in first class over 18 years old

print(df.head())

# create a jittered strip plot with embark_town along the x-axis and age along the
# y-axis. Label the graph "Ages of first-class adult males on the Titanic by point of embarkation"
sns.stripplot(
    data=df,
    x="embark_town",
    y="age",
    hue="embark_town",
)

# Save the image
plt.savefig("titanic_strip_python.png")
