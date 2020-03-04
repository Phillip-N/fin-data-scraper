#! python3
# scraps financial sites for stock data

import requests, bs4, sys
import json

from tickSearch import tickSearch
from getChart import getChart
from getSummary import getSummary

# --------Commands----------
# fds.py q ticker
# fds.py mq tickers #WIP
# fds.py chart ticker
# fds.py summary ticker
# fds.py search companyname
# --------------------------

def getQuote(ticker):
    url = 'https://ca.finance.yahoo.com/quote/%s' % ticker
    req = requests.get(url)
    req.raise_for_status()
    quotesoup = bs4.BeautifulSoup(req.text, features='html.parser')
    quote = quotesoup.select('.Trsdu\(0\.3s\)')
    if req.history:
        print('''
        Sorry, we could not find that a quote for that ticker,
        please try to search for your company using the search
        command scraper.py search 'companyname' to search for
        the correct ticker symbol
        ''')
    else:
        print(f'Price: {quote[0].getText()}')
        print(f'Change: {quote[1].getText()}')


if len(sys.argv) <= 3:
    if sys.argv[1] == 'q':
        getQuote(sys.argv[2])
    elif sys.argv[1] == 'summary':
        getSummary(sys.argv[2])
    elif sys.argv[1] == 'chart':
        getChart(sys.argv[2])
    elif sys.argv[1] == 'search':
        tickSearch(sys.argv[2])

if len(sys.argv) > 3:
    pass
    #TODO add multiple quote checker