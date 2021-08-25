import quandl
# Allows us to work with the Quandl API and use their data pipelines

def get_sentiment():
    """Grabs the cleaned up sentiment Dataframe"""
    quandl.ApiConfig.api_key = 'API_KEY'
    sent = quandl.get("AAII/AAII_SENTIMENT", authtoken="API_KEY")
    # Grabs the dataframe from Quandl
    sent_10 = sent.tail(10)
    # Grabs only the 10 newest columns
    sent_10_trimmed = sent_10[['Bullish', 'Bearish']]
    # Clips off all the columns except for Bullish and Bearish
    final_df = sent_10_trimmed.iloc[::1]
    # Revereses the order so the most recent data appears at the top
    final_df.index = final_df.index.strftime('%m/%d/%y')
    # Changes the date labels into a shorter format so they don't hand off the screen when they are charted
    return final_df


def get_unemployment():
    """ Returns a table of recent new jobless claims"""
    initial = quandl.get("FRED/ICNSA", authtoken="API_KEY")
    # Gets unemployment rate
    flipped = initial.iloc[::1]
    # Reverses the data.
    flipped = flipped.tail(10)
    # Trims off all columns except for the 10 most recent
    flipped.index = flipped.index.strftime('%m/%d/%y')
    # Reformats the dates to be a shorter format
    return flipped

def get_cons():
    """ Returns a dataframe of consumer sentiment """
    get = quandl.get("UMICH/SOC1", authtoken="API_KEY")
    # Gets the consumer sentiment data from the Quandl API
    recent_10 = get.tail(10)
    # Gets the 10 most recent pieces of data and trims the excess
    recent_10.index = recent_10.index.strftime('%m/%d/%y')
    # Reformats the dates in the index to be shorter
    return recent_10
    # Returns a dataframe of the 10 most recent pieces of consumer sentiment data
