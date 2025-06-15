from flask import Flask, render_template, request
from parser import search_hdrezka

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # Получаем поисковый запрос из GET или POST
    query = request.args.get('query') if request.method == 'GET' else request.form.get('query')
    movies = []
    if query:
        try:
            movies = search_hdrezka(query)
        except Exception as e:
            print(f'Ошибка при поиске: {e}')
    return render_template('index.html', movies=movies)

if __name__ == '__main__':
    app.run(debug=True)