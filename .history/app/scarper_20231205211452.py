#Need to import the a web scraper module
from bs4 import BeautifulSoup

#Need to import the requests module to make a request to the website
import requests
#Need to import the time module to allow the program to sleep
import time
#Need to import the json module to allow the program to write to a json file
import json
#Need to import the os module to allow the program to create a directory
import os

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