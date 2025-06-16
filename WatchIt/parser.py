import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://baskino.biz'

def search_baskino(query):
    url = f"{BASE_URL}/index.php?do=search"
    params = {
        "subaction": "search",
        "story": query
    }

    response = requests.post(url, data=params)
    soup = BeautifulSoup(response.text, 'html.parser')
    movies = []

    for item in soup.select('.short'):
        title = item.select_one('.short-title').text.strip()
        image = item.select_one('img')['src']
        link = item.select_one('a')['href']
        movies.append({
            'title': title,
            'image': image,
            'link': link
        })

    return movies
