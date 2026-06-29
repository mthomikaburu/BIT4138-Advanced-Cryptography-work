import http.server, ssl

server_address = ('localhost', 4443)
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)

# Create SSL context
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="server.crt", keyfile="server.key")

# Wrap the socket with SSL
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print("[OK] HTTPS server running on https://localhost:4443")
httpd.serve_forever()
