import pandas as pd

def get_sp500():
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    dfs = pd.read_html(url)
    df = dfs[0]
    symbols = df['Symbol']
    return symbols.tolist()

