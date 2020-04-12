from data1 import *
# Imports everything data1.py without having to reference it every time you call from it
from matplotlib import pyplot as plt
# Library for charting
import os as os

dir = os.path.join(os.getcwd(), 'static')


# Gets the relative file path to the /static/ directory, where all of these functions will place images

def chart_sentiment():
    """Pulls data from get_sentiment() and charts it.
       Saves an image file in the /static/ directory"""
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
    plt.legend(["Bullish", "Bearish"])
    # Adds the legend
    plt.xticks(rotation=90)
    # Rotates the date labels on the y-axis so they don't overlap
    plt.tight_layout()
    # Resizes the window so nothing gets cut off
    fig = plt.gcf()
    # Gets the current figure (Must do this before the file can be saved to an image)
    dir2 = os.path.join(dir, 'sentiment-chart.png')
    # starts creating a file path for the chart image to be stored in (/static/)
    save_img = fig.savefig(dir2, dpi=100)
    # Saves the figure to an image
    plt.close(fig)
    # Closes the file. This prevents plt from thinking all charts are one chart.
    return save_img
    # Has the function bring up the chart on the screen when the function is called.


def chart_unemployment():
    """Pulls data from get_unemployment() and charts it.
       Saves an image file in the /static/ directory"""
    data = get_unemployment()
    # Grabs the unemployment dataframe
    y = data['Value']
    # Sets the y value to the number of new unemployment claims
    x = data.index
    # Sets the x value to the dates
    plt.plot(x, y)
    # Plots the unemployment claims to the chart
    plt.title("# New Unemployment Claims")
    # Titles the chart
    plt.xlabel('Dates')
    # Labels the xaxis
    plt.ylabel('Claims (Million)')
    # Labels the Y axis
    plt.xticks(rotation=90)
    # Rotates the date labels on the X-axis so they dont overlap
    plt.tight_layout()
    # Resizes the window so nothing gets cut off
    fig2 = plt.gcf()
    # Gets the current figure (Must do this before the file can be saved to an image)
    dir2 = os.path.join(dir, 'unemployment-chart.png')
    # Creates the file path to store the chart image file
    save_img = fig2.savefig(dir2, dpi=100)
    # Saves the figure to an image
    plt.close(fig2)
    # Closes the file. This prevents plt from thinking all charts are one chart.
    return save_img
    # Makes it so when the function is called it saves the chart to an image.


def chart_cons():
    data = get_cons()
    # Grabs the datafram for consumer sentiment from data1.py
    y = data['Index']
    # Sets the Index as the Y-axis
    x = data.index
    # Sets the dates as the Y-axis
    plt.plot(x, y)
    # Plots x and Y on the chart
    plt.title("Consumer Sentiment")
    # Gives the chart a title
    plt.ylabel("Index Value")
    # Gives the chart a Y label
    plt.xticks(rotation=90)
    # Rotates the date labels on the X axis so they don't overlap
    plt.tight_layout()
    # Resizes the chart window so nothing gets cut off
    fig3 = plt.gcf()
    # Gets the current figures. Must be done before saving the chart or it will come out blank.
    dir2 = os.path.join(dir, 'cons-chart.png')
    # Creates the full path to the /static/ directory where the file will be placed
    save_img = fig3.savefig(dir2, dpi=100)
    # Saves the image to the /static/ folder
    plt.close(fig3)
    # Closes plt so chart creations don't overlap and mix together
    return save_img
    # Saves the image when the function is called

