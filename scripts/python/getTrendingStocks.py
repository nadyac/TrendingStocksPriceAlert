from bs4 import BeautifulSoup, SoupStrainer
import json
import requests
from requests.exceptions import ProxyError
# This code uses BeautifulSoup to scrape trending stocks on Yahoo Finance.
# There used to be Yahoo Finance API to do this but it was discontinued and 
# so webscraping is one way to still get the same information. 


# store results in a JSON with 2 attributes: StockSymbol and Price
def jsonResults(stocksList):
	return json.dumps(stocksList, indent=4) 

# Make request to YAhoo Finance page and set up BeautifulSoup to parse the response
# SoupStrainer allows us to focus on the parts of the HTML elements that contian our data 
# and then we pass those to BeautifulSoup for parsing what we need.
def scrapeYahooFinance(url):
	try:
		req = requests.get(url)
		data = req.text
		targetData = SoupStrainer(["a","td"])
		soup = BeautifulSoup(data, 'html.parser', parse_only=targetData)
		return soup
	except Error:
		print("An Error Occurred with the Request.", Error)

# Scrape Yahoo Finance and store results in a dictionary which will then 
# be turned into JSON before getting passed back to the UI (when server asks for it)
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
		
