import requests
from bs4 import BeautifulSoup

BASE = "https://baskino.biz"

def search_baskino(query):
    url = f"{BASE}/index.php?do=search"
    r = requests.post(url, data={'subaction':'search','story':query}, headers={'User-Agent':'Mozilla/5.0'})
    soup = BeautifulSoup(r.text, 'html.parser')
    movies = []
    for it in soup.select('.shortstory')[:10]:
        a = it.find('a', class_='short-img')
        title = a['title'] if a else it.find('a').text.strip()
        href = BASE + (a['href'] if a else it.find('a')['href'])
        img = it.find('img')['src'] if it.find('img') else ''
        desc_el = it.find('div', class_='short-story')
        desc = desc_el.text.strip() if desc_el else ''
        movies.append({'title': title, 'url': href, 'image': img, 'desc': desc})
    return movies

def get_player_link(movie_url):
    r = requests.get(movie_url, headers={'User-Agent':'Mozilla/5.0'})
    soup = BeautifulSoup(r.text, 'html.parser')
    iframe = soup.find('iframe')
    return iframe['src'] if iframe else None