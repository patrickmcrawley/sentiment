import pandas as pd
from pprint import pprint
def get_sp500():
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    dfs = pd.read_html(url)
    df = dfs[0]
    symbols = df['Symbol']
    list = symbols.tolist()
    for x in list:
        if not x.isalpha():
            list.remove(x)
    return list


pprint(get_sp500())