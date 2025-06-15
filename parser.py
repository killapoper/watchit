import requests
from bs4 import BeautifulSoup

def search_hdrezka(query):
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f"https://hdrezka.ag/search/?do=search&subaction=search&q={query}"
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    results = []
    for item in soup.select('.b-content__inline_item')[:5]:
        title = item.select_one('.b-content__inline_item-link').text.strip()
        href = item.select_one('.b-content__inline_item-link')['href']
        img = item.select_one('img')['src']
        desc = item.select_one('.b-content__inline_item-cover-descr')
        description = desc.text.strip() if desc else 'Описание отсутствует'
        results.append({
            'title': title,
            'url': href,
            'img': img,
            'desc': description
        })
    return results

def get_video_links(movie_url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(movie_url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    iframe = soup.find('iframe')
    return iframe['src'] if iframe else None