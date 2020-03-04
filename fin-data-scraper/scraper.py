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


def getSummary(ticker):
    pass

def tickSearch(companyname):
    req = requests.get('https://stocks.tradingcharts.com/stocks/symbols/s/all/%s' %companyname)
    req.raise_for_status
    searchsoup = bs4.BeautifulSoup(req.text, features='html.parser')
    table = searchsoup.find('table', {'class':'stocks_symbols_results_table'})

    searchresults = []
    for td in table.find_all('td'):
        if td.find(class_='stocks_symbols_results_table_link') or td.find('a'):
            continue
        else:
            searchresults.append(td.text)
    
    # Format Results
    colCn = searchresults[0:len(searchresults):3]
    colSym = searchresults[1:len(searchresults):3]
    colExc = searchresults[2:len(searchresults):3]

    # Adding Headers
    colCn.insert(0, 'Company Name')
    colSym.insert(0, 'Symbol')
    colExc.insert(0, 'Exchange')

    colWidth = [max(colCn), max(colSym), max(colExc)]

    # Creating Table
    table = [colCn, colSym, colExc]

    # Printing Results





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