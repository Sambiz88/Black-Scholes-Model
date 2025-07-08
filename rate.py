import datetime as dt 
import pandas_datareader.data as web


def get_r(series='DGS3MO') : 
     
    today = dt.date.today()
    start = today - dt.timedelta(days=30)
    r = web.DataReader(series, 'fred', start)['DGS3MO'].dropna().iloc[-1]

    print(f"The current risk-free rate is {r} %")
    return r
