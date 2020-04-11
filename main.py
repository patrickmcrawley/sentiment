from flask import Flask, render_template, url_for, request, redirect
#import quandl
import data1 as d
import pandas as pd
#import unzipper as uz
import os
#import xlrd

#from pathlib import Path

#print('working')
#dirname = os.path.dirname(__file__)
#filename = r'C:\Users\The Rig\PycharmProjects\QuandlProject\testcsv\test.csv'
#Path(os.path.join(dirname, 'testcsv/test.csv'))

app = Flask(__name__)

@app.route('/')
def hello_world():
    if __name__ == '__main__':
        df3 = pd.DataFrame(d.get_sentiment())
        #df = pd.read_csv(r'C:\Users\The Rig\PycharmProjects\QuandlProject\FINRA\FINRA_20200410.csv')
        #df2 = df.tail()
        return df3.to_html()
    #return render_template('table.html', title="Welcome", paragraph='Lorem ipsum dolor sit amet')

if __name__ == '__main__':
    app.run(debug=True)
