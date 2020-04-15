from flask import Flask, render_template, url_for, request, redirect
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
# import quandl
import data1 as d
import pandas as pd
# import unzipper as uz
import os as os
import plots as p

p.chart_cons()
app = Flask(__name__)
Bootstrap(app)
db = SQLAlchemy(app)

db_path = os.path.join(os.path.dirname(__file__), 'SP500.db')
db_uri = 'sqlite:///{}'.format(db_path)
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri

class sandp(db.Model):
    id = db.Column(db.String(5), primary_key=True)
    shortvol = db.Column(db.Integer())

@app.route('/')
def hello_world():
    if __name__ == '__main__':
        #df3 = pd.DataFrame(d.get_sentiment())
        #return plotter.chart_sentiment()
        return render_template('index.html')

        #return df3.to_html()

@app.route('/short')
def short():
    return render_template('short.html')


if __name__ == '__main__':
    app.run(debug=True)
