# TrendingStocksPriceAlert
Get Price Alert for Trending Stocks listed on Yahoo Finance. This app demonstrates features typically seen in hackathon submissions. As such it exemplifies how to make a webapp that fetches live data from a source (Yahoo) and allows the user to interact with it on the webpage. It uses an API, a JS Framework (Angular), and has multiple components in different languages that talk to eachother via common protocols.  

### Play-by-play, this App:
0) Listens for get requests via a python http server
1) Scrapes Yahoo Finance for trending stocks and returns a JSON with the stock symbols and prices
2) Serves returned JSON to UI which is handled by AngularJS
3) Displays the trending stocks so the User can select to receive Price change Alerts for individual stocks via SMS
4) Sends SMS to user after they click a "Set Price Alert" button, notifying them of the price alert for the selected stock

### Features
* Webscraping (python)
* Server with request handlers (python)
* AngularJS framework (JS)
* Twilio API for SMS (Python)


#### Structure

# Project tree
TrendingStocksPriceAlert</br>
&nbsp;&nbsp;&nbsp; + server.py</br>
&nbsp;&nbsp;&nbsp; + index.html</br>
&nbsp;&nbsp;&nbsp; + README.md</br>
&nbsp;&nbsp;&nbsp; + scripts/</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; + python/</br>
<space><space><space>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; +---getTrendingStocks.py</br>
<space><space><space>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; +---SMS.py</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; + js/</br>
<space><space><space>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; +---app.js</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; +style/</br>
<space><space><space>&nbsp;&nbsp;&nbsp; css files borrowed from ColorLib

      
      


