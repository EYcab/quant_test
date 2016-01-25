# For Visualization
#mport matplotlib.pyplot as plt
#%matplotlib inline
# For reading stock data from yahoo
from pandas.io.data import DataReader

# For time stamps
from datetime import datetime

# For division

from scipy.stats import skew, kurtosis

def get_skewness(time_series):
    time_series_skewness = skew(time_series)
    print("Skewness  = %.2f" % time_series_skewness)    
    daily_return=time_series.pct_change()
    daily_return_skewness = skew(daily_return.dropna())
    print("daily_return_skewness  = %.2f" % daily_return_skewness)
    # plt.figure(num=2, figsize=(9, 6))
    # plt.subplot(2, 1, 1)
    # plt.plot(time_series)
    # plt.xlabel("stock_price_skewness")
    # plt.ylabel("Adj Close price")
    # plt.subplot(2, 1, 2)
    # plt.ylabel("daily_return")
    # daily_return.plot(figsize=(12,4),legend=True,linestyle='--',marker='o')
    return time_series_skewness,daily_return_skewness


if __name__ == '__main__':
    stock = 'SINA'
    # Set up End and Start times for data grab
    # 1 yr from now
    end = datetime.now()
    start = datetime(end.year - 1,end.month,end.day)

    globals()[stock] = DataReader(stock,'yahoo',start,end)["Adj Close"]
    # adjusted close price of SINA for now
    adj_close_now=SINA[-1]
    print("asj_close_price_now %s  " % (adj_close_now))
    time_series_skewness,daily_return_skewness= get_skewness(SINA)





