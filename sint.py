import quandl
import pandas as pd
import get_sp500 as sp
import re
import sqlite3
import os

# Order of Operations:
# write_sp500() - (If needed, this takes awhile) - This creates txt file
# SP500_DF() - Populates the database with the most updated values
# read_from_sp500_db() - Returns the 20 highest short interest volume


def write_sp500():
    # Scrapes the curent list of S&P500 companies from wikipedia and combines them with their most recent value for short interest data.
    file = open("SP500_List.txt", "w").close()
    # Wipes the file clean from any prior calls of this function.
    file = open("SP500_List.txt", "a+")
    # Opens the file in append mode so it can be added to line-by-line.
    counter = 0
    # Counter used for the loading print statements
    append_df = pd.DataFrame()
    tickers = sp.get_sp500()
    # Gets all the stock tickers from SP500_List.txt
    for x in tickers:
        sec = str('FINRA/FNSQ_' + x)
        # Template for making individual calls to our Quandl database
        quandl.ApiConfig.api_key = 'kTx7XssV5LbHw4AmPyvf'
        # Our unique API key linked to our quandl accounts
        newest1 = quandl.get(sec).tail(1)
        # Grabs only the single newest piece of data/ row
        newest1['Ticker'] = x
        # Adds the appropriate tickers name to the dataframe
        DataFrame = newest1.drop(['ShortExemptVolume', 'TotalVolume'], axis=1)
        # Trims off excess data we won;t be using
        appended_df = append_df.append(DataFrame)

        file.write(str(appended_df.values) + "\n")
        # Writes the values to our text file line-by-line
        counter += 1
        # Adds to our loading counter every time we iterate over a ticker
        print("{}/500------------------{}".format(counter, str(appended_df.values)))
    file.close()
    return print('Current S&P 500 updated in SP500_List.txt')


def create_db():
    """Creates a new database in the root of the project with columns for 'Ticker' and 'Value',
    This list will be empty and must be populated by running the SP500_DF() function."""
    conn = sqlite3.connect('SP500.db')
    # connects to our sqlite database
    c = conn.cursor()
    # Initiates a cursor for working with our database
    c.execute("""CREATE TABLE IF NOT EXISTS sp500 (Ticker TEXT, Value REAL)""")
    # Creates a table named sp500.db if it doesnt exist already
    conn.commit()
    # Saves changes
    conn.close()
    return print("Database Created: sp500.db")


def SP500_DF():
    """Replaces the sp500 database with a new version with the most updated values"""
    delete_sp500_db()
    create_db()
    # Deletes the database so it can be re-populated with the newest values
    conn = sqlite3.connect('SP500.db')
    # Connects to our database
    c = conn.cursor()
    # Initializes a cursor for working with our database
    file = open("SP500_List.txt", "r")
    # Opens our raw text file of S&P500 companies
    for line in file:
        # Loops through each line in the text file,
        # which contains a ticker and a corresponding value with excess characters
        re_match = re.search(r"\[\[(\d*.0) '([A-Z]*)']]", line)
        # Trims the excess characters off our ticker and value pair
        ticker = re_match.group(2)
        # Captures the ticker from the txt file
        num = re_match.group(1)
        # Captures the value from the txt file.
        c.execute("""INSERT INTO sp500 (Ticker, Value) VALUES ( ?, ? )""", (ticker, num))
        # Puts the data into our SQL database
    conn.commit()
    # Saves changes to our SQL database
    conn.close()


def read_from_sp500_db():
    """Returns a tale of 20 s&p500 companies with the highest shortinterest volume"""
    conn = sqlite3.connect('SP500.db')
    # connects to db
    c = conn.cursor()
    # Initializes a cursor for working with our db
    c.execute("""SELECT * FROM sp500 ORDER BY Value DESC LIMIT 20""")
    # Grabs the top 20 items in our db by highest short volume to lowest
    data = c.fetchall()
    # Allows us to access our data in a variable
    conn.close()
    return data


def delete_sp500_db():
    os.remove('SP500.db')
    return print('sp500.db deleted.')

SP500_DF()
print(read_from_sp500_db())
