#!/usr/bin/python3
import socket
import http.server
import socketserver
PORT = 80
class HTTPServerV6(HTTPServer):
  address_family = socket.AF_INET6

Handler = http.server.SimpleHTTPRequestHandler

server = HTTPServerV6(("::", 80), Handler)
server.serve_forever()