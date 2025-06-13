# from http.server import SimpleHTTPRequestHandler
# from socketserver import TCPServer
# import os
#
# PORT = 8000
#
# # Указываем, где лежат файлы веб-приложения
# os.chdir("webapp")
#
# Handler = SimpleHTTPRequestHandler
#
# with TCPServer(("", PORT), Handler) as httpd:
#     print(f"🚀 Сервер запущен на http://127.0.0.1:{PORT}")
#     httpd.serve_forever()
from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # Render укажет нужный порт
    app.run(host='0.0.0.0', port=port)
