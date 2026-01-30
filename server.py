from http.server import BaseHTTPRequestHandler, HTTPServer
import socket

class SimpleHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello World")

        elif self.path == "/hostname":
            hostname = socket.gethostname()
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(hostname.encode())

        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")

def run(server_class=HTTPServer, handler_class=SimpleHandler, port=80):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


run()