import pandas as pd
import numpy as np
import scipy.stats as stats

df = pd.read_csv("assets/mtcars.csv")  # load the mtcars.csv dataset

mean = np.mean(df['wt'])  # find the mean of the column wt
median = np.median(df['wt'])# find the median of the column wt
mode = np. # find the mode of the column wt

print("mean = {:.5f}, median = {:.3f}, mode = {}".format(mean, median, mode))