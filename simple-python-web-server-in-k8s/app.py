#!/usr/bin/env python3

# Application run as daemon with next rotes:
# “/” with page where it is written  "Success!"
# “/ping” where is written "Ok"
# “/factorial”. Function which calculates factorial of number. The number posted with "POST" to this rote and calculate and return it.


from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO
import socketserver


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Success!")
        elif self.path == "/ping":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Ok")
        else:
            self.send_response(200)
            self.end_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()

        try:
            number = int(body)
            result = 1
            if number >= 0:
                i = 1 
                for i in range (1, int(number)+1):
                    result = result * i
            else:
                result = "Put the positive number or 0"
        except:
            result = "Put the positive number or 0"
            
        response.write(str(result).encode())
        self.wfile.write(response.getvalue())


server_port = 9080
httpd = HTTPServer(('localhost', server_port), SimpleHTTPRequestHandler)
httpd.serve_forever()
