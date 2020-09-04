import http.server
import socketserver

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print ("serving at Port:", PORT)
    httpd.serve_forever()

'''
https://www.afternerd.com/blog/python-http-server/
'''