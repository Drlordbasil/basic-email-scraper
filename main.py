import requests
from bs4 import BeautifulSoup
import re
import csv

class EmailScraper:
    def __init__(self, url):
        self.url = url
        self.emails = []

    def crawl(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup

    def extract_emails(self, soup):
        emails = re.findall(r'[\w\.-]+@[\w\.-]+', soup.text)
        return emails

    def validate_emails(self, emails):
        valid_emails = []
        for email in emails:
            if re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
                valid_emails.append(email)
        return valid_emails

    def scrape(self):
        soup = self.crawl()
        emails = self.extract_emails(soup)
        valid_emails = self.validate_emails(emails)
        self.emails = valid_emails
        return self.emails

    def save_to_csv(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Email'])
            for email in self.emails:
                writer.writerow([email])

# Example usage
scraper = EmailScraper('https://github.com/Drlordbasil')
emails = scraper.scrape()
print(emails)
scraper.save_to_csv('emails.csv')
