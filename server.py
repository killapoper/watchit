from flask import Flask, render_template, request
from parser import search_baskino, get_player_link

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    q = request.args.get('q', '')
    movies = search_baskino(q) if q else []
    return render_template('index.html', movies=movies, query=q)

@app.route('/watch')
def watch():
    url = request.args.get('url', '')
    video = get_player_link(url)
    return render_template('player.html', video_link=video)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)