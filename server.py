import time
from http.server import HTTPServer, SimpleHTTPRequestHandler
from scripts.python.getTrendingStocks import getTrendingTickers
from scripts.python.SMS import setAlert

HOST_NAME = 'localhost'
PORT_NUMBER = 8000

class MyHandler(SimpleHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        if "getStocks" in self.path:
        	# here is the code for getting stocks
            # whatever we send to "responsd" as an argument will be sent back
            # we can retrieve stocks within this scope and then pass info to self.respond
            content = getTrendingTickers()
            self.respond(content)
        elif "setAlert" in self.path:
        	#TODO add params for phoneNumber and stock symbol
        	content = setAlert(str(self.path))
        	self.respond("OK")
        else:
            super(MyHandler, self).do_GET()

    def handle_http(self, data):
        self.send_response(200)
        # set the data type for the response header. In this case it will be json.
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        return bytes(data, 'UTF-8')

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