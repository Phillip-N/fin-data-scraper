import requests, bs4

def tickSearch(companyname):
    req = requests.get('https://stocks.tradingcharts.com/stocks/symbols/s/all/%s' %companyname)
    req.raise_for_status
    searchsoup = bs4.BeautifulSoup(req.text, features='html.parser')
    table = searchsoup.find('table', {'class':'stocks_symbols_results_table'})

    # Print not found message if company not found
    if table == None:
        print('''
        Company not found, please note this function
        only currently supports US and Canadian
        companies.
        ''')

    # Else print results
    else:
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

        # Finding appropiate column widths
        cN = [len(i) for i in colCn]
        sym = [len(i) for i in colSym]
        exc = [len(i) for i in colExc]

        colWidth = [max(cN), max(sym), max(exc)]

        # Creating Table
        table = [colCn, colSym, colExc]

        # Printing Results
        for i in range(len(table[0])): 
            for y in range(3):
                if (y != 0) and ((y % 2) == 0):
                    print(table[y][i].ljust(colWidth[y]))
                else:
                    print(table[y][i].ljust(colWidth[y]), end=' ')
