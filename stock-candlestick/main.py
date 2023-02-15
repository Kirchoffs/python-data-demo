import configparser
import tushare as ts
import matplotlib.pyplot as plt
from matplotlib.dates import date2num
import mplfinance as mpf
from mplfinance.original_flavor import candlestick_ohlc
import datetime

def date_to_num(dates):
    dates_num = []
    for date in dates:
        date_time = datetime.datetime.strptime(date, '%Y%m%d')
        date_num = date2num(date_time)
        dates_num.append(date_num)
    return dates_num

config_file = './config.ini'
config_parser = configparser.ConfigParser()
config_parser.read(config_file, encoding = 'utf-8')
config = dict(config_parser.items('tushare'))

ts.set_token(config['tushare_token'])
pro = ts.pro_api()

df = pro.query('daily', ts_code = '000002.SZ', start_date = '20190601', end_date = '20190930')
df['MA5'] = df['close'].rolling(5).mean()
df['MA10'] = df['close'].rolling(10).mean()
print(df)
df_arr = df.to_numpy()
df_arr[:,1] = date_to_num(df_arr[:,1])
df_arr = df_arr[:,1:]

fig, axes = plt.subplots(2, 1, sharex = True, figsize = (15, 8))
ax1, ax2 = axes.flatten()

candlestick_ohlc(ax1, df_arr, width = 0.6, colorup = 'r', colordown = 'g', alpha = 1.0)
ax1.plot(df_arr[:,0], df['MA5'])
ax1.plot(df_arr[:,0], df['MA10'])
ax1.set_title('Stock General Chart')
ax1.set_xlabel('Date')
ax1.set_ylabel('Price')
ax1.grid(True)
ax1.xaxis_date()

ax2.bar(df_arr[:,0], df_arr[:,8])
ax2.set_title('Stock Trading Volume')
ax2.set_xlabel('Date')
ax2.set_ylabel('Volume')
ax2.grid(True)
ax2.xaxis_date()

plt.show()
