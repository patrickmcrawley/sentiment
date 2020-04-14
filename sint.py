import quandl
import pandas as pd
import datetime

from pandas import DataFrame

import get_sp500 as sp

#quandl.ApiConfig.api_key = 'kTx7XssV5LbHw4AmPyvf'
#print(quandl.get("FINRA/FNYX_AAPL", authtoken="kTx7XssV5LbHw4AmPyvf"))

append_df = pd.DataFrame()
tickers = sp.get_sp500()
for x in tickers:
    #print('FINRA/FORF_' + x)
    sec = str('FINRA/FNSQ_' + x)
    quandl.ApiConfig.api_key = 'kTx7XssV5LbHw4AmPyvf'
    newest1 = quandl.get(sec).tail(1)
    newest1['Ticker'] = x
    DataFrame = newest1.drop(['ShortExemptVolume', 'TotalVolume'], axis=1)
    print(DataFrame)
    appended_df = append_df.append(DataFrame)





