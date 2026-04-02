from http.server import SimpleHTTPRequestHandler, HTTPServer

port = 8000

server = HTTPServer(("0.0.0.0", port), SimpleHTTPRequestHandler)
print(f"Server running on port {port}")
server.serve_forever()