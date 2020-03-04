import requests, bs4

def getSummary(ticker):
    req = requests.get('https://ca.finance.yahoo.com/quote/%s' % ticker)
    req.raise_for_status()
    sumsoup = bs4.BeautifulSoup(req.text, features='html.parser')

    # Previous Close
    ele = sumsoup.find(attrs={"data-test": "PREV_CLOSE-value"})
    pClose = ele.find('span').text

    # Open
    ele = sumsoup.find(attrs={"data-test": "OPEN-value"})
    _open = ele.find('span').text

    # 52-week range
    f2week = sumsoup.find(attrs={"data-test": "FIFTY_TWO_WK_RANGE-value"}).text

    # Volume
    ele = sumsoup.find(attrs={"data-test": "TD_VOLUME-value"})
    vol = ele.find('span').text

    # Avg Volume
    ele = sumsoup.find(attrs={"data-test": "AVERAGE_VOLUME_3MONTH-value"})
    avgvol = ele.find('span').text

    # Market Cap
    ele = sumsoup.find(attrs={"data-test": "MARKET_CAP-value"})
    mc = ele.find('span').text

    # PE (TTM)
    ele = sumsoup.find(attrs={"data-test": "PE_RATIO-value"})
    pe = ele.find('span').text

    # EPS
    ele = sumsoup.find(attrs={"data-test": "EPS_RATIO-value"})
    eps = ele.find('span').text

    # 1-Year Target
    ele = sumsoup.find(attrs={"data-test": "ONE_YEAR_TARGET_PRICE-value"})
    tar = ele.find('span').text

    print(f'''
    Previous Close: {pClose}
    Open: {_open}
    52-Week Range: {f2week}
    Volume: {vol}
    Avg Vol: {avgvol}
    Market Cap: {mc}
    PE Ratio: {pe}
    EPS: {eps}
    1-Year Target: {tar}
    ''')