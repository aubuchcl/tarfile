#!/usr/bin/python3
import http.server
import socketserver
PORT = 80

Handleer = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handleer) as httpd:
  print('serving')
  httpd.serve_forever()
