#!/usr/bin/python3

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            # Send a response status code (200 means "OK")
            self.send_response(200)

            # Send headers (extra info about the response)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()  # finish sending headers

            # Write the actual message back to the browser
            message = "Hello, this is a simple API!"
            # convert string → bytes before sending
            self.wfile.write(message.encode())

        elif self.path == "/data":
            dataset = {"name": "John", "age": 30, "city": "New York"}
            body = json.dumps(dataset)

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            self.wfile.write(body.encode())

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"404 Not Found")


server = HTTPServer(("", 8000), Handler)
print("Server running on http://localhost:8000")
server.serve_forever()
