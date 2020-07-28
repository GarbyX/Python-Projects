
# Stack Abuse - Introduction to Web Scraping with Python
# beautiful = urllib2.urlopen(url).read()

# Step 1 - Downloading HTML [Using HTTP Libraries]

# $ pip install requests
# And now you can use it in your code, like this:

import requests
import csv
result = requests.get('http://quotes.toscrape.com/')
page = result.text

# Step 2 - Parsing HTML and Extracting Data

# Now, let's start parsing the HTML page using BeautifulSoup. But first, we must install it:

# $ pip install beautifulsoup4
# Once installed, you can call it in your code like this:

from bs4 import BeautifulSoup
soup = BeautifulSoup(page, 'html.parser')

# $ pip install beautifulsoup4

quotes = soup.find_all('div', class_='quote')

scraped = []
for quote in quotes:
    text = quote.find('span', class_='text').text
    author = quote.find('small', class_='author').text
    scraped.append([text, author])

# Step 3 - Storing the Retrieved Data


with open('quotes.csv', 'w') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
for quote in scraped:

    writer.writerow(quote)



















