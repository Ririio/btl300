import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

titanic = pd.read_csv("assets/titanic.csv")


sns.set_theme(style="whitegrid", color_codes=True)

plt.title("Titanic passengers by class", fontsize=20)

sns.countplot(x="class", color="b", data=titanic)

plt.show()

sns.countplot(y="class", color="b", data=titanic)

plt.show()
