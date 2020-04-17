import pandas as pd
import sqlite3
import get_sp500 as sp
import quandl
import os


def write_sp500():
    conn = sqlite3.connect('SP500.db')
    # connects to our sqlite database
    c = conn.cursor()
    c.execute"""DROP TABLE IF EXISTS SP500"""
    # Initiates a cursor for working with our database
    print("Committing changes to database...")
    conn.commit()
    print("Closing database connection...")
    conn.close()
    print("Done.")
    print("Clearing old database...")
    #os.remove('SP500.db')
    print("Creating new database...")
    #open('SP500.db', 'a').close()
    counter = 0
    # Counter used for the loading print statements
    append_df = pd.DataFrame()
    print("Gathering tickers...")
    tickers = sp.get_sp500()
    # Gets all the stock tickers from SP500_List.txt
    print("Connecting to database...")
    conn = sqlite3.connect('SP500.db')
    # connects to our sqlite database
    c = conn.cursor()
    # Initiates a cursor for working with our database
    print("Creating table in database...")
    c.execute("""CREATE TABLE IF NOT EXISTS sp500 (Ticker TEXT, Value REAL)""")
    # Creates a table named sp500.db if it doesnt exist already
    print("Looping through all current companies in S&P500...")
    for x in tickers:
        print("{}/500 - Requesting data for {} from Quandl...".format(counter, x))
        sec = str('FINRA/FNSQ_' + x)
        # Template for making individual calls to our Quandl database
        quandl.ApiConfig.api_key = 'kTx7XssV5LbHw4AmPyvf'
        # Our unique API key linked to our quandl accounts
        print("{}/500 - Getting newest data for {} from Quandl...".format(counter, x))
        newest1 = quandl.get(sec).tail(1)
        # Grabs only the single newest piece of data/ row
        print("{}/500 - Storing {} ticker in memory...".format(counter, x))
        newest1['Ticker'] = x
        # Adds the appropriate tickers name to the dataframe
        print("{}/500 - Trimming off excess data for {}....".format(counter, x))
        DataFrame = newest1.drop(['ShortExemptVolume', 'TotalVolume'], axis=1)
        # Trims off excess data we won;t be using
        print("{}/500 - Initializing temporary DataFrame for {}...".format(counter, x))
        appended_df = append_df.append(DataFrame)
        print("{}/500 - Storing short volume for {} in memory...".format(counter, x))
        shortVolume = float(DataFrame['ShortVolume'])
        print("{}/500 - Short volume for {} is {}.....".format(counter, x, shortVolume))
        counter += 1
        print("{}/500 - Storing [ {} , {} ] in database...".format(counter, x, shortVolume))
        c.execute("""INSERT INTO sp500 (Ticker, Value) VALUES ( ?, ? )""", (x, shortVolume))
    print("Committing changes to database...")
    conn.commit()
    print("Closing database connection...")
    conn.close()
    print("Done.")

    return print('Current S&P 500 updated in SP500_List.txt')

