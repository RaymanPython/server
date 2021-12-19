from http.server import HTTPServer, CGIHTTPRequestHandler
server_address = ("", 8005) #например, на порту 8000
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
httpd.serve_forever()


