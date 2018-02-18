#!/usr/bin/python3
import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
from scripts.python.getTrendingStocks import getTrendingTickers
hostName = ""
hostPort = 8000

class MyServer(BaseHTTPRequestHandler):
    #	GET request is for client to get data from backend script through the server.
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.send_header('Content-Length', str(len(open('index.html').read())))
        self.end_headers()
        self.wfile.write(bytes(open('index.html').read(), "utf-8"))

        # self.wfile.write(bytes("<html><p>You accessed path: %s</p></html>" % self.path, "utf-8"))

    #	POST request is for submitting data to the backend through the server. 
    def do_POST(self):
        print("incomming http: ", self.path)

        #if self.path =='/':
        	#send stock
        #else self.path == '/postDate':
        	#other stuff

        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        post_data = self.rfile.read(content_length)  # <--- Gets the data itself
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        content = getTrendingTickers()
        self.send_header('Content-Length', len(content))
        self.end_headers()
        self.wfile.write(bytes(content, 'utf-8'))


myServer = HTTPServer((hostName, hostPort), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))

