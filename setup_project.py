from flask import Flask, render_template, request, redirect, url_for
from parser import search_movies, get_player_link

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    query = request.args.get("query")
    movies = []

    if query:
        try:
            movies = search_movies(query)
        except Exception as e:
            print(f"Ошибка при поиске фильмов: {e}")
            movies = []

    return render_template("index.html", movies=movies)

@app.route("/watch/<path:movie_url>")
def watch(movie_url):
    try:
        video_link = get_player_link(movie_url)
        return render_template("player.html", video_link=video_link)
    except Exception as e:
        print(f"Ошибка при получении ссылки на видео: {e}")
        return "Ошибка загрузки видео", 500

if __name__ == "__main__":
    app.run(debug=True)