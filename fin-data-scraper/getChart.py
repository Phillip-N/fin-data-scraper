import requests, bs4, os
from PIL import Image

def getChart(ticker):
    os.makedirs('charts', exist_ok=True)
    req = requests.get('https://web.tmxmoney.com/legacy-charting.php?qm_symbol=%s' %ticker)
    req.raise_for_status
    chartsoup = bs4.BeautifulSoup(req.text, 'html.parser')

    table = chartsoup.find('table')
    chartElem = table.find('img')

    if chartElem == []:
        print('Could not find chart, please make sure you type US symbols with :US at the end')
    else:
        chartUrl = chartElem.get('src')
        res = requests.get(chartUrl)
        res.raise_for_status
    
        image = open(os.path.join('charts', os.path.basename(chartUrl)), 'wb')
        for chunk in res.iter_content(100000):
            image.write(chunk)
        image.close

