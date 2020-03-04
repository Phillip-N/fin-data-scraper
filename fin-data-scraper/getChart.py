import requests, bs4, os
from PIL import Image

def getChart(ticker):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}
    os.makedirs('charts', exist_ok=True)
    req = requests.get('https://stockcharts.com/h-sc/ui?s=%s' %ticker, headers=headers)
    req.raise_for_status
    chartsoup = bs4.BeautifulSoup(req.text, 'html.parser')

    chartElem = chartsoup.select('#chartImg')

    if chartElem == []:
        print('Could not find chart please make sure you typed in the right company, ticker')
    else:
        chartUrl = 'https:' + chartElem[0].get('src')
        res = requests.get(chartUrl, headers=headers)
    
        image = open(os.path.join('charts', 'sc.png'), 'wb')
        for chunk in res.iter_content(100000):
            image.write(chunk)
        image.close

        img = Image.open(r'.\charts\sc.png')
        img.show()
