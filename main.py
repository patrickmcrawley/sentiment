from flask import Flask, render_template, url_for, request, redirect
# import quandl
import data1 as d
import pandas as pd
# import unzipper as uz
import os

app = Flask(__name__)


@app.route('/')
def hello_world():
    if __name__ == '__main__':
        df3 = pd.DataFrame(d.get_sentiment())

        return df3.to_html()


if __name__ == '__main__':
    app.run(debug=True)
