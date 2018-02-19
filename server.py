import time
from http.server import HTTPServer, SimpleHTTPRequestHandler
from scripts.python.getTrendingStocks import getTrendingTickers
from scripts.python.SMS import setAlert

HOST_NAME = 'localhost'
PORT_NUMBER = 8000

# This class contains methods to handle our requests to different URIs in our app
class MyHandler(SimpleHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    # Check the URI of the request to serve the proper content.
    def do_GET(self):
        if "getStocks" in self.path:
        	# If URI contains getStocks, execute the code for getting stocks
            # whatever we send to "respond" as an argument will be sent back to client
            content = getTrendingTickers()
            self.respond(content) # we can retrieve stocks within this scope and then pass info to self.respond
        elif "setAlert" in self.path: 
        	# params for phoneNumber and stock symbol are contained in the URI/path of get request
        	# i.e. the request is something like localhost:8000?setAlert=[symbol]&toNumber=[phone#]
        	# we can parse this request path to get the params.
        	content = setAlert(str(self.path))
        	self.respond({"response":"OK"})
        else:
            super(MyHandler, self).do_GET()

    def handle_http(self, data):
        self.send_response(200)
        # set the data type for the response header. In this case it will be json.
        # setting these headers is important for the browser to know what to do with
        # the response. Browsers can be very picky this way.
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        return bytes(data, 'UTF-8')

     # store response for delivery back to client. This is good to do so
     # the user has a way of knowing what the server's response was.
    def respond(self, data):
        response = self.handle_http(data)
        self.wfile.write(response)

if __name__ == '__main__':
    server_class = HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print(time.asctime(), 'Server Starts - %s:%s' % (HOST_NAME, PORT_NUMBER))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(time.asctime(), 'Server Stops - %s:%s' % (HOST_NAME, PORT_NUMBER))