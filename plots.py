from data1 import *
# Imports everything data1.py without having to reference it every time you call from it
from matplotlib import pyplot as plt
# Library for charting
import pandas as pd
# Library for data manipulation

def chart_sentiment():
    """Pulls data from get_sentiment and charts it"""
    data = get_sentiment()
    # Uses our sentiment data for the data set
    y1 = data['Bullish']
    # Assigns Y-axis data for Bullish
    y2 = data['Bearish']
    # Assigns Y-axis data for bearish
    x = data.index
    # Assigns the dates as the index
    plt.plot(x, y1)
    # Plots bullish
    plt.plot(x, y2)
    # Plots bearish
    plt.xlabel('Dates')
    # Labels the X axis with Dates
    plt.ylabel(' ')
    # Leaves the Y axis label blank
    plt.title('Sentiment')
    # Titles the chart as Sentiment
    plt.legend(["Bullish","Bearish"])
    # Adds the legend
    plt.xticks(rotation=90)
    # Rotates the date labels on the y-axis so they don't overlap
    sentiment_chart = plt.show()
    # Brings the chart up on the screen
    return sentiment_chart
    # Has the function bring up the chart on the screen when the function is called.

# print(get_unemployment())

#def chart_unemployment():
#    data = get_unemployment()
#    y = data['Value']
#    x = data.index
#    plt.plot(x, y)

