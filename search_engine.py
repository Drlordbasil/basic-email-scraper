import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus

class SearchEngine:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

    def search_google(self, query, num_results=10):
        search_url = f"https://www.google.com/search?q={quote_plus(query)}&num={num_results}"
        response = requests.get(search_url, headers=self.headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        search_results = soup.find_all('div', class_='yuRUbf')
        return [result.find('a')['href'] for result in search_results if result.find('a')]

    def search_bing(self, query, num_results=10):
        search_url = f"https://www.bing.com/search?q={quote_plus(query)}&count={num_results}"
        response = requests.get(search_url, headers=self.headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        search_results = soup.find_all('li', class_='b_algo')
        return [result.find('a')['href'] for result in search_results if result.find('a')]
