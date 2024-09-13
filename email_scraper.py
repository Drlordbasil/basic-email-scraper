import requests
from bs4 import BeautifulSoup
import re
import csv
from search_engine import SearchEngine

class EmailScraper:
    def __init__(self, search_query):
        self.search_query = search_query
        self.emails = set()
        self.search_engine = SearchEngine()

    def crawl(self, url):
        try:
            response = requests.get(url, headers=self.search_engine.headers, timeout=10)
            return BeautifulSoup(response.text, 'html.parser')
        except:
            return None

    def extract_emails(self, soup):
        return re.findall(r'[\w\.-]+@[\w\.-]+', soup.text)

    def validate_emails(self, emails):
        return [email for email in emails if re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email)]

    def scrape_website(self, url):
        soup = self.crawl(url)
        if soup:
            emails = self.extract_emails(soup)
            valid_emails = self.validate_emails(emails)
            self.emails.update(valid_emails)

    def scrape(self):
        google_results = self.search_engine.search_google(self.search_query)
        bing_results = self.search_engine.search_bing(self.search_query)
        all_urls = list(set(google_results + bing_results))

        for url in all_urls:
            self.scrape_website(url)

        return list(self.emails)

    def save_to_csv(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Email'])
            for email in self.emails:
                writer.writerow([email])
