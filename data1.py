import quandl
#from numpy import recarray
#from pandas import DataFrame


def get_sentiment():
    """Grabs the cleaned up sentiment Dataframe"""

    quandl.ApiConfig.api_key = 'kTx7XssV5LbHw4AmPyvf'
    #data = quandl.get("FINRA/FNRA_AAPL", authtoken="kTx7XssV5LbHw4AmPyvf")
    sent = quandl.get("AAII/AAII_SENTIMENT", authtoken="kTx7XssV5LbHw4AmPyvf")
    # Grabs the dataframe from Quandl

    sent_10 = sent.tail(10)
    # Grabs only the 10 newest columns

    sent_10_trimmed = sent_10[['Bullish', 'Bearish']]
    # Clips off all the columns except for Bullish and Bearish

    final_df = sent_10_trimmed.iloc[::-1]
    # Revereses the order so the most recent data appears at the top

    return final_df


#In progress

# def get_cons():
#    cons = quandl.get('UMICH/SOC22')
#    """Get's consumer sentiment"""
#
#    print(cons.columns)

##get_cons()


def get_unemployment():
    """ Returns a table of recent new jobless claims"""
    initial = quandl.get("FRED/ICNSA", authtoken="kTx7XssV5LbHw4AmPyvf")
    # Gets unemployment rate

    flipped = initial.iloc[::-1]
    # Reverses the data.

    flipped = flipped.head(10)
    # Trims off all columns except for the 10 most recent

    return flipped
