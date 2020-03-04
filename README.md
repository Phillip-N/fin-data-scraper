# fin-data-scraper
Financial Data Web Scraper

<h3>User Guide</h3>

<ol>
  <li> Add the directory where you keep the scraper to PATH</li>
  <li> Modify the .bat file to include the file path to the directory as well</li>
  <li> You can now run the below commands directly from the Run app (Win + R)
</ol>

<table style="width:100%">
  <tr>
    <th>Commands</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>fds q {ticker}</td>
    <td>Returns the current stock price as well as the change from the prior day's close</td>
  </tr>
  <tr>
    <td>fds search {companyname}</td>
    <td>Returns a table of company names matching the query, along with their tickers and exchange</td>
  </tr>
  <tr>
    <td>fds summary {ticker}</td>
    <td>Returns a snapshot summary of the given stock</td>
  </tr>
  <tr>
    <td>fds chart {ticker}</td>
    <td>Opens an image snapshot of the stock chart, based on given ticker</td>
  </tr>
  <tr>
    <td>fds mq {ticker(s)}</td>
    <td>Returns a list of multiple quotes based on the ticker query</td>
  </tr>
    
