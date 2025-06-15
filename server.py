# # # from flask import Flask, render_template
# # # import os
# # #
# # # app = Flask(__name__)
# # #
# # # @app.route('/')
# # # def home():
# # #     return render_template('index.html')
# # #
# # # @app.route('/film/<int:id>')
# # # def film(id):
# # #     return render_template('film.html', id=id)
# # #
# # # if __name__ == '__main__':
# # #     app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))
# # # from flask import Flask, request, jsonify
# # # from parser import search_hdrezka, get_video_links
# # #
# # # app = Flask(__name__)
# # #
# # # @app.route('/search_hdrezka')
# # # def search():
# # #     query = request.args.get('query')
# # #     if not query:
# # #         return jsonify({'error': 'Missing query'}), 400
# # #
# # #     results = search_hdrezka(query)
# # #     enriched = []
# # #
# # #     for r in results:
# # #         video_url = get_video_links(r['url'])
# # #         if video_url:
# # #             enriched.append({
# # #                 'title': r['title'],
# # #                 'poster': '/static/default-poster.jpg',  # если постер с hdrezka недоступен, временно заглушка
# # #                 'source': video_url
# # #             })
# # #
# # #     return jsonify({'results': enriched})
# # from flask import Flask, request, jsonify
# # from parser import search_hdrezka, get_video_links
# # import os
# #
# # app = Flask(__name__, static_folder='static', template_folder='templates')
# #
# # @app.route('/')
# # def index():
# #     return app.send_static_file('index.html')
# #
# # @app.route('/search_hdrezka')
# # def search():
# #     query = request.args.get('query', '')
# #     if not query:
# #         return jsonify({'results': []})
# #     results = search_hdrezka(query)
# #     enriched = []
# #     for r in results:
# #         video_src = get_video_links(r['url'])
# #         if video_src:
# #             enriched.append({
# #                 'title': r['title'],
# #                 'poster': '',  # после можно добавить парсинг постера
# #                 'source': video_src
# #             })
# #     return jsonify({'results': enriched})
# #
# # if name == "__main__":
# #     port = int(os.environ.get("PORT", 5000))
# #     app.run(host='0.0.0.0', port=port)
#
#
# from flask import Flask, render_template, request
# from parser import search_hdrezka, get_video_links
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def index():
#     return render_template('index.html')
#
#
# @app.route('/film')
# def film():
#     query = request.args.get('query')
#     results = search_hdrezka(query)
#
#     if not results:
#         return render_template('film.html', title="Фильм не найден", video_url=None)
#
#     title = results[0]['title']
#     url = results[0]['url']
#     video_url = get_video_links(url)
#
#     return render_template('film.html', title=title, video_url=video_url)
# from flask import Flask, render_template, request
# from parser import search_hdrezka, get_video_links
#
# app = Flask(__name__, static_folder='static', template_folder='templates')
#
#
# @app.route('/')
# def index():
#     return render_template('index.html')
#
#
# @app.route('/search')
# def search():
#     query = request.args.get('q', '')
#     if not query:
#         return render_template('index.html', results=[])
#
#     results = search_hdrezka(query)
#     return render_template('index.html', results=results, query=query)
#
#
# @app.route('/watch')
# def watch():
#     url = request.args.get('url')
#     if not url:
#         return "Нет ссылки на фильм", 400
#
#     video_link = get_video_links(url)
#     if not video_link:
#         return "Видео не найдено", 404
#
#     return render_template('watch.html', video_link=video_link)
from flask import Flask, render_template, request, jsonify
from parser import search_hdrezka, get_video_links

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def index():
    # Фильмы по умолчанию
    default_movies = [
        {"title": "Интерстеллар", "poster": "/static/img/interstellar.jpg", "url": "/watch?title=Интерстеллар"},
        {"title": "Начало", "poster": "/static/img/inception.jpg", "url": "/watch?title=Начало"},
        {"title": "Матрица", "poster": "/static/img/matrix.jpg", "url": "/watch?title=Матрица"},
        {"title": "Остров проклятых", "poster": "/static/img/shutter_island.jpg", "url": "/watch?title=Остров проклятых"},
        {"title": "Аватар", "poster": "/static/img/avatar.jpg", "url": "/watch?title=Аватар"},
        {"title": "Титаник", "poster": "/static/img/titanic.jpg", "url": "/watch?title=Титаник"},
        {"title": "Темный рыцарь", "poster": "/static/img/dark_knight.jpg", "url": "/watch?title=Темный рыцарь"},
        {"title": "Дюна", "poster": "/static/img/dune.jpg", "url": "/watch?title=Дюна"},
        {"title": "Гравитация", "poster": "/static/img/gravity.jpg", "url": "/watch?title=Гравитация"},
        {"title": "Хоббит", "poster": "/static/img/hobbit.jpg", "url": "/watch?title=Хоббит"},
    ]
    return render_template("index.html", movies=default_movies)

@app.route('/search')
def search():
    query = request.args.get('q', '')
    if not query:
        return jsonify([])

    results = search_hdrezka(query)
    return jsonify(results)

@app.route('/watch')
def watch():
    url = request.args.get('url')
    if not url:
        return "Нет ссылки на фильм", 400

    video_link = get_video_links(url)
    if not video_link:
        return "Видео не найдено", 404

    return render_template('film.html', video_link=video_link)