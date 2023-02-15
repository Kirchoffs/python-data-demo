import configparser
import matplotlib.pyplot as plt
import tushare as ts

config_file = './config.ini'
config_parser = configparser.ConfigParser()
config_parser.read(config_file, encoding = 'utf-8')
config = dict(config_parser.items('tushare'))

ts.set_token(config['tushare_token'])
pro = ts.pro_api()

df = pro.query('daily', ts_code = '000002.SZ', start_date = '20090101', end_date = '20190101')
print(df.head())

# df.to_excel('stock-data.xlsx', index = False)
# df.set_index('trade_date', inplace = True)
# df['close'].plot(title = 'Vanke stock trend')
# plt.show()

from datetime import datetime
df['trade_date'] = df['trade_date'].apply(lambda date: datetime.strptime(date, '%Y%m%d'))
plt.plot(df['trade_date'], df['close'])
plt.show()