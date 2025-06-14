from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/film/<int:id>')
def film(id):
    return render_template('film.html', id=id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))
from flask import Flask, request, jsonify
from parser import search_hdrezka, get_video_links

app = Flask(__name__)

@app.route('/search_hdrezka')
def search():
    query = request.args.get('query')
    if not query:
        return jsonify({'error': 'Missing query'}), 400

    results = search_hdrezka(query)
    enriched = []

    for r in results:
        video_url = get_video_links(r['url'])
        if video_url:
            enriched.append({
                'title': r['title'],
                'poster': '/static/default-poster.jpg',  # если постер с hdrezka недоступен, временно заглушка
                'source': video_url
            })

    return jsonify({'results': enriched})