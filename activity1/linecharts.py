# import the pandas module
import pandas as pd
import matplotlib.pyplot as plt

tgt = pd.read_csv("assets/target.csv")  # load the target.csv file

tgt_march = tgt.tail(19)  # subset the last 19 days of the dataframe

tgt_vol = tgt_march[
    ["Date", "Volume"]
]  # subset tgt_march and create a data frame that contains the columns: Date and Volume

tgt_close = tgt_march[
    ["Date", "Close"]
]  # subset tgt_march and create a data frame that contains the columns: Date and Close

day = int(input()) - 1

volume_row = tgt_vol.iloc[day]  # subset the specific row of tgt_vol for the given day
volume = volume_row.iloc[1]  # gets the volume for the given day

close_row = tgt_close.iloc[
    day
]  # subset the specific row of tgt_close for the given day
close = close_row.iloc[1]  # gets the closing stock price for the given day

date = tgt_march.iloc[day].iloc[0]  # gets the date

print("The volume of TGT on " + str(date) + " is " + str(int(volume)) + ".")
print("The closing stock price of TGT on " + str(date) + " is $" + str(close) + ".")

# add title: Target (TGT) closing stock price
plt.title("Target (TGT) closing stock price")
# add Date as the xlabel and Stock price (USD) as the ylabel
plt.xlabel("Date")
plt.ylabel("Stock price (USD)")
plt.xticks(rotation=55)
# plot the line chart for closing stock price
plt.plot(tgt_close["Date"], tgt_close["Close"])

plt.show()

# add title: Target (TGT) volume
plt.title("Target (TGT) volume")
# add Date as the xlabel and Volume as the ylabel
plt.xlabel("Date")
plt.ylabel("Volume")
# rotate xticks by 55 degrees
plt.xticks(rotation=55)
# plot the line chart for volume
plt.plot(tgt_vol["Date"], tgt_vol["Volume"])

plt.show()
