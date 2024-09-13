from email_scraper import EmailScraper

def main():
    search_query = 'i am lonely'
    scraper = EmailScraper(search_query)
    emails = scraper.scrape()
    print(emails)
    scraper.save_to_csv('emails.csv')

if __name__ == "__main__":
    main()
