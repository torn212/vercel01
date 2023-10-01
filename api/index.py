from http.server import BaseHTTPRequestHandler
import cgi


class handler(BaseHTTPRequestHandler):


    def do_GET(self):
        form = cgi.FieldStorage
        name = form.getvalue('name', '')
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(name+" aaaaaaaaa   ".encode())
        return
