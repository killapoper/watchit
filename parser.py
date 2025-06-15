
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0'
}

def search_hdrezka(query):
    search_url = f'https://hdrezka.ag/search/?do=search&subaction=search&q={query}'
    r = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    results = []
    for item in soup.select('.b-content__inline_item'):
        try:
            title = item.select_one('.b-content__inline_item-link').text.strip()
            url = item.select_one('.b-content__inline_item-link')['href']
            image = item.select_one('img')['src']
            description = item.select_one('.b-content__inline_item-link + div').text.strip()
            results.append({
                'title': title,
                'url': url,
                'image': image,
                'description': description
            })
        except:
            continue

    return results[:10]  # limit to 10 results

def get_video_links(movie_page_url):
    r = requests.get(movie_page_url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    iframe = soup.find('iframe')
    if iframe:
        return iframe['src']
    return None
