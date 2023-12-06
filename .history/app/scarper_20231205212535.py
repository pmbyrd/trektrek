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

dax = requests.get("https://memory-alpha.fandom.com/wiki/Jadzia_Dax")
dax_html = dax.text

soup_dax = BeautifulSoup(dax_html, 'html.parser')
