#! python3
# scraps financial sites for stock data

import requests, bs4, sys
import json

from tickSearch import tickSearch

#TODO Create comments detailing possible sys commands
#TODO Download webpage containing financial data with requests
    #TODO Stock Price and Summary through YAHOO FINANCE given Ticker
    #TODO If failed give message prompting user to search for company
        #TODO Company search will use https://stocks.tradingcharts.com/stocks/symbols/s/all/ to look for potential matchese
        #TODO Store matches in dictionary, and output on screen
    #TODO Use TMX legacy charts and pillow to download yearly charts
#TODO Parse HTML bs4
#TODO Return relevant data based on sys args

# Commands
# fds q ticker
# fds mq tickers 
# fds chart ticker
# fds summary ticker
# fds search companyname

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


def getSummary(ticker):
    pass

def getChart(ticker):
    pass

if len(sys.argv) <= 3:
    if sys.argv[1] == 'q':
        getQuote(sys.argv[2])
    elif sys.argv[1] == 'summary':
        pass
    elif sys.argv[1] == 'chart':
        pass
    elif sys.argv[1] == 'search':
        tickSearch(sys.argv[2])

if len(sys.argv) > 3:
    pass