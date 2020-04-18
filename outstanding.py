from typing import List, Any

from yahooquery import Ticker
import get_sp500 as sp
import pandas as pd
import os as os
import sqlite3

d = []

def share_values():
    """Shits out a fat chart"""

    print("Connecting to SQL database...")
    conn = sqlite3.connect('SP500.db')
    c = conn.cursor()
    print("Wiping yesterday's table...")
    c.execute('''DROP TABLE IF EXISTS key_stats''')
    print("Saving...")
    conn.commit()
    print("Closing")
    conn.close()
    print("Getting current S&P500 tickers...")
    tickers = sp.get_sp500()
    print("Reconecting to SQL database...")
    with sqlite3.connect('SP500.db') as conn:
        c = conn.cursor()
        print("Creating table key_stats in SP500.db...")
        c.execute('''CREATE TABLE IF NOT EXISTS key_stats (tickers TEXT, shares_outstanding INTEGER, short_interest INTEGER, float INTEGER, market_cap INTEGER, industry TEXT)''')
        print("Looping through data...")
        for x in tickers:
            ticks = Ticker(x)
            stockvalues = ticks.key_stats
            details = ticks.summary_detail
            profile = ticks.summary_profile
            for key, value in stockvalues.items():
                try:
                    global sos_values
                    sos_values = value['sharesOutstanding']
                    print("[{}] sos: {}".format(x, sos_values))
                    global short_int
                    short_int = value['sharesShort']
                    print("[{}] sin: {}".format(x, short_int))
                    global float
                    float = value['floatShares']
                    print("[{}] flt: {}".format(x, float))
                except:
                    #print('error stockvalues {}'.format(x))
                    continue
                #d.append({'ticker': x, 'OS': sos_values, 'short': short_int, 'float': float})
            details = ticks.summary_detail
            for key, value in details.items():
                try:
                    global mcap
                    mcap = value['marketCap']
                    print("[{}] mkc: {}".format(x, mcap))
                    #c.execute('''INSERT INTO key_stats (market_cap) VALUES (?)''', (mcap))
                except:
                    #print('error market cap {}'.format(x))
                    continue
            profile = ticks.summary_profile
            for key, value in profile.items():
                try:
                    global industry
                    industry = value['industry']
                    print("[{}] ind: {}".format(x, industry))
                    #c.execute('''INSERT INTO key_stats (industry) VALUES (?)''', (str(industry)))
                except:
                    print('industry error {}'.format(x))
                    continue


            c.execute('''INSERT INTO key_stats (tickers, shares_outstanding, short_interest, float, market_cap, industry) VALUES (?, ?, ?, ?, ?, ?)''', (str(x), int(sos_values), int(short_int), int(float), int(mcap), str(industry)))
            print('-------------------------------------')

        conn.commit()
        c.execute('''SELECT * FROM key_stats''')
        result = c.fetchall()
        return result

def read_share_values():
    with sqlite3.connect('SP500.db') as conn:

        df = pd.read_sql("""SELECT * FROM key_stats ORDER BY tickers ASC""", conn)
        df['short_percent'] = df['short_interest'] / df['float']
        return df













