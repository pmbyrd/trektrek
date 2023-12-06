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

r2 = requests.get("https://memory-alpha.fandom.com/wiki/Portal:Main")
r_html2 = r2.text

soup2 = BeautifulSoup(r_html2, 'html.parser')

titles2 = soup2.find_all('a')