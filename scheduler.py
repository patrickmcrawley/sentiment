import data1 as d
import get_sp500 as sp
import plots as p
import sint as s
import time
import schedule



def job():
    """Schedules the newest data to be grabbed every night at midnight."""
    d.get_cons()
    print("Getting investor sentiment data...")
    d.get_sentiment()
    print("Getting consumer sentiment data...")
    d.get_unemployment()
    print("Getting unemployment data...")
    sp.get_sp500()
    print("Getting current S&P500 companies...")
    p.chart_cons()
    print("Charting investor sentiment...")
    p.chart_sentiment()
    print("Charting consumer sentiment...")
    p.chart_unemployment()
    print("Charting unemployment...")
    s.delete_sp500_db()
    print("Clearing old database...")
    s.write_sp500()
    print("Writing short volume data to database...")
    return print("Done.")


schedule.every().day.at("16:55").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)