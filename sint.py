import quandl
import pandas
import datetime

#quandl.ApiConfig.api_key = 'kTx7XssV5LbHw4AmPyvf'
#print(quandl.get("FINRA/FNYX_AAPL", authtoken="kTx7XssV5LbHw4AmPyvf"))


list = ['AAPL', 'NFLX']
for x in list:

    #print('FINRA/FORF_' + x)
    sec = str('FINRA/FNSQ_' + x)
    print(sec)
    quandl.ApiConfig.api_key = 'kTx7XssV5LbHw4AmPyvf'
    print(quandl.get(sec))


