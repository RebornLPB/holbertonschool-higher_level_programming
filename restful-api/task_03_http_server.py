#!/usr/bin/python3
"""
Simple HTTP Server using Python's http.server module.
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """
    Custom request handler inheriting from BaseHTTPRequestHandler
    to serve custom endpoints and handle GET requests.
    """

    def do_GET(self):
        """Handle HTTP GET requests and route them based on self.path."""
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == '/data':
            sample_data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(sample_data).encode('utf-8'))

        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == '/info':
            info_data = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(info_data).encode('utf-8'))

        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"404 Not Found")


def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    """Start the HTTP server on port 8000."""
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server.")
        httpd.server_close()


if __name__ == '__main__':
    run()
