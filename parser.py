from hdrezka import Search
from hdrezka.api.http import login_global
import os, asyncio

# Если сайт HDRezka требует обход Cloudflare, можно настроить login
# os.environ['LOGIN_NAME']='ваш_логин'
# os.environ['LOGIN_PASSWORD']='ваш_пароль'
# asyncio.run(login_global(os.environ['LOGIN_NAME'], os ... ))

async def get_search_results(query):
    results = await Search(query).get_page(1)
    movies = []
    for item in results[:10]:
        player = await item.player
        movies.append({
            'title': item.title,
            'url': item.url,
            'img': item.thumbnail,
            'desc': item.description or '—',
            'player_url': await player.get_stream(1, 1, None)
        })
    return movies

def search_hdrezka(query):
    return asyncio.run(get_search_results(query))