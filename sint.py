import quandl
import pandas
import datetime
import get_sp500 as sp

#quandl.ApiConfig.api_key = 'kTx7XssV5LbHw4AmPyvf'
#print(quandl.get("FINRA/FNYX_AAPL", authtoken="kTx7XssV5LbHw4AmPyvf"))


tickers = sp.get_sp500()
for x in tickers:
    #print('FINRA/FORF_' + x)
    sec = str('FINRA/FNSQ_' + x)
    print(sec)
    quandl.ApiConfig.api_key = 'kTx7XssV5LbHw4AmPyvf'
    print(quandl.get(sec).head())


