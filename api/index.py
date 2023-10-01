from http.server import BaseHTTPRequestHandler

from flask import request


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        name = request.args.get("name")
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(name + " aaaaaaaaa   ".encode())
        return
