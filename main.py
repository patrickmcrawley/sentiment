from flask import Flask, render_template, url_for, request, redirect
from flask_bootstrap import Bootstrap
# import quandl
import data1 as d
import pandas as pd
# import unzipper as uz
import os as os
import plots as plotter
import plots as p


app = Flask(__name__)
Bootstrap(app)



@app.route('/')
def hello_world():
    if __name__ == '__main__':
        #df3 = pd.DataFrame(d.get_sentiment())
        #return plotter.chart_sentiment()
        return render_template('index.html')

        #return df3.to_html()


if __name__ == '__main__':
    app.run(debug=True)
