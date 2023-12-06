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

titles_dax = soup_dax.find_all('h2')

for t in titles_dax:
    print(t.text)

print("----------------------------------------")

print("https://memory-alpha.fandom.com/wiki/Jadzia_Dax?file=Jadzia_Dax%2C_2369.jpg")
print("https://static.wikia.nocookie.net/memoryalpha/images/5/5c/Jadzia_Dax%2C_2374.jpg/revision/latest?cb=20061228060458&path-prefix=en")

aside = soup.find_all('aside')
aside_htm