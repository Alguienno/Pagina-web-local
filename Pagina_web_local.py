from http.server import HTTPServer, BaseHTTPReque>
from sys import argv

text = ' '.join(argv[2:])

class SimpleHTTPRequestHandler(BaseHTTPRequestHan>

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(text.encode())


if __name__ == "__main__":

        httpd = HTTPServer(('localhost',int(argv[
