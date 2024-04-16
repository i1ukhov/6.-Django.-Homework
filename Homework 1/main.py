from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import os

hostName = "localhost"
serverPort = 8080
path_os = os.path.dirname(os.path.abspath(__file__))
file_name = os.path.join(path_os, 'index.html')


class MyServer(BaseHTTPRequestHandler):

    @staticmethod
    def __get_index():
        """Метод получения страницы из html-файла"""
        with open(file_name, 'r', encoding='utf-8') as f:
            result = f.read()
        return result

    def do_GET(self):
        query_components = parse_qs(urlparse(self.path).query)
        print(query_components)
        page_content = self.__get_index()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(page_content, "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
