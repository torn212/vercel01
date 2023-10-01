from http.server import BaseHTTPRequestHandler

import flask
from flask import Flask


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        name = flask.request.args.get('name')
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(name + " aaaaaaaaa   ".encode())
        return
