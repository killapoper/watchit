from flask import Flask, render_template, request
from parser import search_hdrezka, get_video_links

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get('q', '')
    if not query:
        return render_template('index.html', results=[])

    results = search_hdrezka(query)
    return render_template('index.html', results=results, query=query)

@app.route('/watch')
def watch():
    url = request.args.get('url')
    if not url:
        return "Нет ссылки на фильм", 400

    video_link = get_video_links(url)
    if not video_link:
        return "Видео не найдено", 404

    return render_template('watch.html', video_link=video_link)