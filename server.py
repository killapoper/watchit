# server.py
from flask import Flask, render_template, request, redirect, url_for
from parser import search_hdrezka, get_video_link

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get('q', '')
    if not query:
        return redirect(url_for('index'))
    results = search_hdrezka(query)
    return render_template('results.html', movies=results, query=query)

@app.route('/watch')
def watch():
    url = request.args.get('url')
    if not url:
        return redirect(url_for('index'))
    video_url = get_video_link(url)
    if not video_url:
        return "Видео не найдено 😢"
    return render_template('player.html', video_url=video_url)