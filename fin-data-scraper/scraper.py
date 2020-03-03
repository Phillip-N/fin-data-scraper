#! python3
# scraps financial sites for stock data

import requests, bs4, sys
import json

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
    req = requests.get('https://ca.finance.yahoo.com/quote/%s' % ticker)
    req.raise_for_status()
    quotesoup = bs4.BeautifulSoup(req.text, features='html.parser')
    quote = quotesoup.select('.Trsdu\(0\.3s\)')
    print(f'Price: {quote[0].getText()}')
    print(f'Change: {quote[1].getText()}')


def getSummary(ticket):


if len(sys.argv) <= 3:
    if sys.argv[1] == 'q':
        getQuote(sys.argv[2])
    elif sys.argv[1] == 'summary':
        pass
    elif sys.argv[1] == 'chart':
        pass
    elif sys.argv[1] == 'search':
        pass

if len(sys.argv) > 3:
    pass