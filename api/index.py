from http.server import BaseHTTPRequestHandler
from flask import Flask,request


class handler(BaseHTTPRequestHandler):


    def do_GET(self):
        name = request.GET.get('name')
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(name+" aaaaaaaaa   ".encode())
        return
