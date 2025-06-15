# parser.py
from HdRezkaApi import HdRezkaSearch, HdRezkaApi

def search_hdrezka(query):
    try:
        pages = HdRezkaSearch("https://hdrezka.ag/")(query, find_all=False)
        items = pages.first
        res = []
        for it in items[:10]:
            res.append({
                'title': it['title'],
                'url': it['url'],
                'img': it['image'],
                'desc': ''
            })
        return res
    except Exception as e:
        print("Ошибка поиска:", e)
        return []

def get_video_link(movie_url):
    try:
        api = HdRezkaApi(movie_url)
        if not api.ok:
            return None
        stream = api.getStream()
        return stream('720p') or stream('480p') or stream('360p') or None
    except Exception as e:
        print("Ошибка получения видео:", e)
        return None