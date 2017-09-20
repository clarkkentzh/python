#coding=utf-8
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer


class Zhao(BaseHTTPRequestHandler):
    def do_GET(self):
        print "hello world"
        print self.rfile.read()
        self.wfile.write("hahahahahaah")
        return
    def do_POST(self):
        return

address = ("127.0.0.1",3000)
server = HTTPServer(address,Zhao)
server.serve_forever()
