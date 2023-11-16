import os
import pandas as pd
import toolkit_config as cfg

QAN_PRC_CSV = os.path.join(cfg.DATADIR, 'qan_prc_2020.csv')
QAN_NOHEAD_CSV = os.path.join(cfg.DATADIR, 'qan_prc_no_header.csv')
QAN_CLOSE_CSV = os.path.join(cfg.DATADIR, 'qan_close_ser.csv')

# Reading data from a CSV file
qan_naive_read = pd.read_csv(QAN_PRC_CSV)
print(qan_naive_read)
qan_naive_read.info()

# Using the `set_index` method
qan_naive_read.set_index('Date', inplace=True)
print(qan_naive_read)
qan_naive_read.info()

# Using the `index_col` parameter
qan_better_read = pd.read_csv(QAN_PRC_CSV, index_col='Date')
print(qan_better_read)
qan_better_read.info()

# Storing data to a CSV file
qan_better_read = pd.read_csv(QAN_PRC_CSV, index_col='Date')
qan_better_read.to_csv(QAN_NOHEAD_CSV, header=False)

# Saving the contents of a series to a CSV file
qan_better_read = pd.read_csv(QAN_PRC_CSV, index_col='Date')
ser = qan_better_read.loc[:, 'Close']
print(ser)
ser.to_csv(QAN_CLOSE_CSV)
print(ser.name)

# Create a series without a name
dates = list(qan_better_read.index)
data = list(qan_better_read.Close)
ser_no_name = pd.Series(data, index=dates)
print(ser_no_name)
print(f'The name of the series is {ser_no_name.name}')

# Now save it to the same CSV file as above
ser_no_name.to_csv(QAN_CLOSE_CSV)

# Read the data back
as_df = pd.read_csv(QAN_CLOSE_CSV)
print(as_df)

# Saving the contents of an unnamed series (better version)
ser_no_name.to_csv(QAN_CLOSE_CSV, header=False)
as_df = pd.read_csv(QAN_CLOSE_CSV, header=None, index_col=0)
print(as_df)

# Saving the contents of an unnamed series (even better version)
ser_no_name.to_csv(QAN_CLOSE_CSV, header=False)
as_df = pd.read_csv(QAN_CLOSE_CSV, header=None, names=["Date", "Close"], index_col=0)
print(as_df)

# Saving the contents of an unnamed series (best version)
ser_no_name.to_csv(QAN_CLOSE_CSV, index_label="Date", header=['Close'])
as_df = pd.read_csv(QAN_CLOSE_CSV, index_col=0)
print(as_df)
