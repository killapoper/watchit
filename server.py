from flask import Flask, render_template, request
from parser import search_hdrezka, get_video_links

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html', results=None, query=None)

@app.route('/search')
def search():
    query = request.args.get('q', '')
    results = search_hdrezka(query) if query else []
    return render_template('index.html', results=results, query=query)

@app.route('/watch')
def watch():
    url = request.args.get('url', '')
    video_link = get_video_links(url)
    return render_template('watch.html', video_link=video_link)