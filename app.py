from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path in ["/", "/index.html", "/index/"]:
            filename = "templates/catalog/index.html"
        elif self.path in ["/catalog/", "/catalog.html"]:
            filename = "templates/catalog/catalog.html"
        elif self.path in ["/category/", "/category.html"]:
            filename = "templates/catalog/category.html"
        elif self.path in ["/contacts/", "/contacts.html"]:
            filename = "templates/catalog/contacts.html"
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write("<h1>404 - Страница не найдена</h1>".encode("utf-8"))
            return

        try:
            with open(filename, 'rb') as f:
                content = f.read()
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(content)
        except FileNotFoundError:
            self.send_response(404)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write("<h1>404 - Файл не найден</h1>".encode("utf-8"))

    def do_POST(self):
        if self.path == "/submit":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = urllib.parse.parse_qs(post_data.decode('utf-8'))

            print("\nНовое сообщение с формы:")
            print(f"Имя: {data.get('name', [''])[0]}")
            print(f"Email: {data.get('email', [''])[0]}")
            print(f"Сообщение: {data.get('message', [''])[0]}")

            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            response_html = (
                "<h2>Спасибо! Ваше сообщение отправлено.</h2>"
                "<a href='/contacts/'>Назад</a>"
            )
            self.wfile.write(response_html.encode("utf-8"))
        else:
            self.send_response(501)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write("<h1>501 - Метод не поддерживается</h1>".encode("utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print(f"Server started http://{hostName}:{serverPort}")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
