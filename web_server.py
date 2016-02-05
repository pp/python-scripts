"""
This is a simple web server. It runs through each URL pattern
in the 'urls' variable and stops at the first one that matches
the requested URL.
"""

import re
from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = 'localhost'
hostPort = 4567

urls = [
    [r'^/?$', 'index'],
    [r'^/test/?$', 'test'],
    [r'^/app/?$', 'app'],
]

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        matched = False

        for x in urls:
            pattern = re.compile(x[0])
            if pattern.match(self.path):
                message = x[1]
                matched = True
                break

        if matched:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes('''
                <p><strong>Welcome to {0}</strong><br>
                Request Method: {1}<br>
                Request Path: {2}</p>'''
                .format(message, self.command, self.path), 'utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes('''
                <p><strong>Not Found (404)</strong><br>
                Request Method: {0}<br>
                Request Path: {1}</p>'''
                .format(self.command, self.path), 'utf-8'))

myServer = HTTPServer((hostName, hostPort), MyServer)

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()
