# TrendingStocksPriceAlert
Get Price Alert for Trending Stocks listed on Yahoo Finance. As a webapp that fetches live data and allows the user to interact with it via a webpage, this project demonstrates features typically seen in hackathon submissions. It uses an API (Twilio), a JS Framework (Angular), and has multiple components in different languages that talk to eachother via common protocols.  

### Play-by-play, this App:
* Listens for get requests via a python http server
* Scrapes Yahoo Finance for trending stocks and returns a JSON with the stock symbols and prices
* Serves returned JSON to UI which is handled by AngularJS
* Displays the trending stocks so the User can select to receive Price change Alerts for individual stocks via SMS
* Sends SMS to user after they click a "Set Price Alert" button, notifying them of the price alert for the selected stock

### Features
* Webscraping via BeautifulSoup(python)
* Server with request handlers (python)
* AngularJS framework (JS)
* Twilio API for SMS (Python)

### Installs Needed for the Project
* <a href="https://www.python.org/downloads/release/python-364/">Python 3</a>
* <a href="https://www.twilio.com/">Twilio API Python helper</a>

## APP IMAGES & HOW-TO

#### 1) Run the python http server. 
* Go to the root directory and run server.py on the terminal or cmd
      * You will see the server output its start time.
      * App will run on 127.0.0.1:8000 </br>
      
<a href="https://imgur.com/nm8Ly88"><img src="https://i.imgur.com/nm8Ly88.png" title="source: imgur.com" /></a>

#### 2) Go to the Homepage for the app.
* In your browser, type 127.0.0.1:8000 in the search bar. This is where the homepage is served.
* As soon as the page is loaded you should see the stocks load. You may verify that they are
accurate by going to <a href="http://finance.yahoo.com/trending-tickers>this Yahoo Finance page</a></br>

<a href="https://imgur.com/NkEPC1U"><img src="https://i.imgur.com/NkEPC1U.png" title="source: imgur.com" /></a>

### 3) Type in your phone number in the input box at the top of the page.
<a href="https://imgur.com/9Llk7tz"><img src="https://i.imgur.com/9Llk7tz.png" title="source: imgur.com" /></a>

### 4) Click on the 'Set Price Alert' button for any stock you want to follow.
* You will get an SMS text message from your Twilio phone number with a confirmation message that you set up the price alert.

<a href="https://imgur.com/JLlVl9F"><img src="https://i.imgur.com/JLlVl9F.png" title="source: imgur.com" /></a>

### Appendix
=============
#### Twilio API Python handler. 
* This is all the code needed to send a simple text message. Note, you need to use your own SID (not mine which is shown in the picture). Naturally you must also use your own secret API key.

<a href="https://imgur.com/dLaHb8N"><img src="https://i.imgur.com/dLaHb8N.png" title="source: imgur.com" /></a>

#### Project tree
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



      
      


