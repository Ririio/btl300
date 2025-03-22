import pandas as pd
import scipy.stats as st
# also import the scipy.stats module.

NBA2019_df = pd.read_csv('assets/NBA2019.csv') # load the dataset in NBA2019.csv

# input desired column. Ex: AGE, 2P%, or PointsPerGame.
chosen_column = input()

NBA2019_df_column = NBA2019_df[[chosen_column]]# create subset of NBA2019_df based on input.

sample_s = st.tstd(NBA2019_df_column)[0] # find standard deviation
sample_s_rounded = round(sample_s, 2) # round to two decimal places

# Output
print('The standard deviation for', chosen_column, 'is:', sample_s_rounded)