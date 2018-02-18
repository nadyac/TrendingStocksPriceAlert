from bs4 import BeautifulSoup, SoupStrainer
import json
import requests
from requests.exceptions import ProxyError

def jsonResults(stocksList):
	return json.dumps(stocksList, indent=4)

def scrapeYahooFinance(url):
	try:
		req = requests.get(url)
		data = req.text
		targetData = SoupStrainer(["a","td"])
		soup = BeautifulSoup(data, 'html.parser', parse_only=targetData)
		return soup
	except Error:
		print("An Error Occurred with the Request.")
	
def getTrendingTickers():
	soup = scrapeYahooFinance("http://finance.yahoo.com/trending-tickers")
	stockSymbols = []
	for a in soup.find_all('a', class_="Fw(b)"):
		stockSymbols.append(a.get_text())

	stockPrices = []
	for b in soup.find_all('td', class_="data-col2 Ta(end) Pstart(20px)"):
		stockPrices.append(b.get_text())

	trendingStocksList = []
	for i in range(len(stockSymbols)):
		trendingStock = {}
		trendingStock["StockSymbol"] = stockSymbols[i]
		trendingStock["Price"] = stockPrices[i]
		trendingStocksList.append(trendingStock)

	return jsonResults(trendingStocksList)
		

#getTrendingTickers()
