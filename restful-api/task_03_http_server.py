#!/usr/bin/python3
"""Develop a simple API using Python with the `http.server` module"""
import http.server, json


class Handler(http.server.BaseHTTPRequestHandler):
    """Start of subclass"""

    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            sample = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(sample).encode("utf-8"))

        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            sample = {"version": "1.0",
                    "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(sample).encode("utf-8"))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"Endpoint Not Found")

PORT = 8000

with http.server.HTTPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
