# Test HTTP server returning always 204 on /
from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"
serverPort = 8080

def mime_type(a_path):
    if ".css" in a_path: return "text/css"
    if ".js" in a_path: return "text/javascript"
    if ".html" in a_path: return "text/html"

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        with open(f"./{self.path}", 'rb') as f:
            f.seek(0,2)
            size = f.tell()
            f.seek(0,0)
            self.protocol_version = 'HTTP/1.1'
            self.send_response(200)
            self.send_header("content-security-policy", "default-src 'self' https://cdn.jsdelivr.net/npm/@siemens/ix@1.1.0/ https://cdn.jsdelivr.net/npm/@siemens/ix-icons@1.0.1/")
            self.send_header("content-length", str(size))
            self.send_header("content-type", mime_type(self.path))
            self.end_headers()
            while True:
                b = f.read(8192)
                if b:
                    self.wfile.write(b)
                else:
                    return

if __name__ == "__main__":
    print("Starting server http://%s:%s" % (hostName, serverPort))
    webServer = HTTPServer((hostName, serverPort), MyServer)

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        print("stop")

    webServer.server_close()
    print("Server stopped.")
