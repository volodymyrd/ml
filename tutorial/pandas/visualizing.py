import datetime
from pandas_datareader import data as web
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

start = datetime.datetime(2017, 7, 1)
end = datetime.datetime(2018, 1, 1)

att = web.DataReader('AAPL', 'google', start, end)
print(att.head())
att['Open'].plot()
plt.legend()
plt.show()