# Import necessary libraries
from bs4 import BeautifulSoup
import pandas as pd
from newsplease import NewsPlease
import json
import requests
import csv

# Scraping multiple articles
# Get the sitemap
source = requests.get('https://www.theguardian.com/sitemaps/news.xml').text
soup = BeautifulSoup(source, 'lxml')

# Extract URLs and last modified dates
locs = []
dates = []
for url in soup.find_all('url'):
    loc = url.find('loc').text
    lastmod = url.find('lastmod').text
    locs.append(loc)
    dates.append(lastmod)

# Store the links in a DataFrame
data_links = pd.DataFrame({'URL': locs, 'Last Modified Date': dates})
#print(len(data_links))

# Prepare the CSV file for saving scraped data
csv_file = open('guardian_data.csv', 'w', newline='', encoding='utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Headline', 'Article Body', 'Author Name', 'Date Published', 'Language', 'Source', 'URL'])

# Scraping function
def scrap_data_using_json_schema(pages_df):
    print("Start The Scrapping | THE GUARDIAN | 300 Articles")
    articles_scraped = 0
    for index, row in pages_df.iterrows(): 
        page = row['URL']
        article = NewsPlease.from_url(page)
        author_name = [article.authors]
        article_body = [article.maintext]
        date_published = [article.date_publish]
        source = [article.source_domain]
        headline = [article.title]
        url = [article.url]
        language = [article.language]
        
        csv_writer.writerow([headline, article_body, author_name, date_published, language, source, url])
        
        articles_scraped += 1
        if articles_scraped == 300:
            break
        
            
    return "All Articles Scraped"

# Execute scraping
guardian_news = scrap_data_using_json_schema(data_links)
print(guardian_news)

# Close the CSV file
csv_file.close()

# Load and print the dataset from CSV
dataset = pd.read_csv("guardian_data.csv")
#print(dataset)
