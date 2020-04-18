from flask import Flask, render_template, url_for, request, redirect
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
# import quandl
from pandas import DataFrame

import data1 as d
import pandas as pd
# import unzipper as uz
import os as os
import plots as p
import sqlite3
import SP500_to_DB as SP500DB
import outstanding as outstanding




db = sqlite3.connect('SP500.db')
#Connects the db to the python file
df = pd.read_sql_query('''SELECT * FROM sp500 ORDER BY Value DESC LIMIT 20''', db)
#Creates dataframe of top 20 most shorted in SP500.db
#db.close()
app = Flask(__name__)
Bootstrap(app)
#db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    if __name__ == '__main__':
        #df3 = pd.DataFrame(d.get_sentiment())
        #return plotter.chart_sentiment()
        return render_template('index.html')

        #return df3.to_html()

@app.route('/short')
def short():
    #x = SP500DB.pull_SP500()
    x = outstanding.read_share_values()
    return render_template('short.html', tables=[x.to_html(index=False, classes=["table-bordered", "table-striped", "table-hover"], header=True)], titles='tickers')
# return render_template('short.html', tables=[df.to_html(index=False, classes=["table-bordered", "table-striped", "table-hover"], header="true")], titles='tickers')



if __name__ == '__main__':
    app.run(debug=False)
