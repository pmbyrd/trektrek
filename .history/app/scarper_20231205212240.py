# Python
from bs4 import BeautifulSoup
import requests

# Make a request to the website
r = requests.get('https://www.nytimes.com')
r_html = r.text

# Create a BeautifulSoup object and specify the parser
soup = BeautifulSoup(r_html, 'html.parser')

# Find all the article titles on the NYTimes front page
titles = soup.find_all('h2')

# Print each title
for title in titles:
    print(title.text)

