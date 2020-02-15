#!/usr/bin/env python3

# Application run as daemon with next rotes:
# “/” with page where it is written  "Success!"
# “/ping” where is written "Ok"
# “/factorial”. Function which calculates factorial of number. The number posted with "POST" to this rote and calculate and return it.


from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO
import socketserver
import math

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        if self.path == "/":
            self.wfile.write(b"Success!")
        elif self.path == "/ping":
            self.wfile.write(b"Ok")

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()

        try:
            number = int(body)
            result = math.factorial(number)
        except:
            result = "Non-negative number required"
            
        response.write(str(result).encode())
        self.wfile.write(response.getvalue())


server_port = 9080
httpd = HTTPServer(('localhost', server_port), SimpleHTTPRequestHandler)
httpd.serve_forever()
