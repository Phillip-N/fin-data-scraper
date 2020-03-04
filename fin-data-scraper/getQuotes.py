import requests, bs4

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

def getMulti(tickers):
    for ticker in tickers:
        url = 'https://ca.finance.yahoo.com/quote/%s' % ticker
        req = requests.get(url)
        req.raise_for_status()
        quotesoup = bs4.BeautifulSoup(req.text, features='html.parser')
        quote = quotesoup.select('.Trsdu\(0\.3s\)')
        if req.history:
            print('Quote not found')
        else:
            print(f'Quote for {ticker.upper()}')
            print(f'Price: {quote[0].getText()}')
            print(f'Change: {quote[1].getText()}' + '\n')