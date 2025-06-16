from flask import Flask, render_template, request
from parser import search_baskino

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    query = request.args.get('query')
    movies = []
    if query:
        movies = search_baskino(query)
    return render_template('results.html', movies=movies)

@app.route('/watch/<path:video_link>')
def watch(video_link):
    return render_template('player.html', video_link=video_link)

if name == '__main__':
    app.run(debug=True)
