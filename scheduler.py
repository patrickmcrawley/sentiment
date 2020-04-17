import data1 as d
import plots as p
import SP500_to_DB as SP500
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
    p.chart_cons()
    print("Charting investor sentiment...")
    p.chart_sentiment()
    print("Charting consumer sentiment...")
    p.chart_unemployment()
    print("Charting unemployment...")
    SP500.write_sp500()
    return print("Done.")


schedule.every().day.at("18:41").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)