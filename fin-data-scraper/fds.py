#! python3
# scraps financial sites for stock data

import sys

from tickSearch import tickSearch
from getChart import getChart
from getSummary import getSummary
from getQuotes import getQuote, getMulti

# --------Commands----------
# fds.py q ticker
# fds.py mq tickers #WIP
# fds.py chart ticker
# fds.py summary ticker
# fds.py search companyname
# --------------------------

if len(sys.argv) <= 3:
    if sys.argv[1] == 'q':
        getQuote(sys.argv[2])
    elif sys.argv[1] == 'summary':
        getSummary(sys.argv[2])
    elif sys.argv[1] == 'chart':
        getChart(sys.argv[2])
    elif sys.argv[1] == 'search':
        tickSearch(sys.argv[2])

if len(sys.argv) > 3 and sys.argv[1] == 'mq':
    getMulti(sys.argv[2:])