import requests
from bs4 import BeautifulSoup


def search_hdrezka(query):
    headers = {
        'User-Agent': 'Mozilla/5.0',
    }
    search_url = f'https://hdrezka.ag/search/?do=search&subaction=search&q={query}'
    r = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    results = []
    for item in soup.select('.b-content__inline_item')[:5]:  # первые 5 результатов
        title = item.select_one('.b-content__inline_item-link').text.strip()
        href = item.select_one('.b-content__inline_item-link')['href']
        results.append({'title': title, 'url': href})
    return results


def get_video_links(movie_page_url):
    headers = {
        'User-Agent': 'Mozilla/5.0',
    }
    r = requests.get(movie_page_url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    iframe = soup.find('iframe')
    if iframe:
        return iframe['src']  # ссылка на плеер

    return None
