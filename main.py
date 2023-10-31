from http.server import BaseHTTPRequestHandler, HTTPServer

hostname = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):

    def __get_html_content(self):
        with open('index.html', 'r', encoding='utf-8') as file:
            file = file.read()
            return file

    def do_GET(self):
        page_content = self.__get_html_content()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(page_content, "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostname, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostname, serverPort))
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.serve_cloce()
    print("Server stop!")
