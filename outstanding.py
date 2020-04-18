from yahooquery import Ticker
import get_sp500 as sp
import pandas as pd
import os as os
import sqlite3

d = []

def share_values():
    conn = sqlite3.connect('SP500.db')
    c = conn.cursor()
    c.execute('''DROP TABLE IF EXISTS key_stats''')
    conn.commit()
    conn.close()
    tickers = sp.get_sp500()
    with sqlite3.connect('SP500.db') as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS key_stats (tickers TEXT, shares_outstanding INTEGER, short_interest INTEGER, float INTEGER, market_cap INTEGER, industry TEXT)''')
        sos_values = 0
        short_int = 0
        float = 0
        mcap = 0
        industry = ''
        for x in tickers:
            ticks = Ticker(x)
            print('getting key statistics {}'.format(x))
            stockvalues = ticks.key_stats
            details = ticks.summary_detail
            profile = ticks.summary_profile
            for key, value in stockvalues.items():
                try:
                    sos_values = value['sharesOutstanding']
                    short_int = value['sharesShort']
                    float = value['floatShares']
                except:
                    print('error stockvalues {}'.format(x))
                    continue
                d.append({'ticker': x, 'OS': sos_values, 'short': short_int, 'float': float})
            # details = ticks.summary_detail
            # for key, value in details.items():
            #     try:
            #         mcap = value['marketCap']
            #         c.execute('''INSERT INTO key_stats (market_cap) VALUES (?)''', (int(mcap)))
            #     except:
            #         print('error market cap {}'.format(x))
            #         continue
            # profile = ticks.summary_profile
            # for key, value in profile.items():
            #     try:
            #         industry = value['industry']
            #         c.execute('''INSERT INTO key_stats (industry) VALUES (?)''', (str(industry)))
            #     except:
            #         print('industry error {}'.format(x))
            #         continue
        print('We are writing to the DB now')
        #c.execute('''INSERT INTO key_stats (tickers, shares_outstanding, short_interest, float, market_cap, industry) VALUES (?, ?, ?, ?, ?, ?)''', (str(x), int(sos_values), int(short_int), int(float), int(mcap), str(industry)))
        conn.commit()
        c.execute('''SELECT * FROM key_stats''')
        result = c.fetchall()
        return result


share_values()
df = pd.DataFrame(d)
print(df)

def write_to_sql():
    conn = sqlite3.connect('SP500.db')
    df.to_sql('key_stats', conn, if_exists='replace', index=False)
    pd.read_sql('select * from key_stats', conn)

write_to_sql()












