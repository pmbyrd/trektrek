# Need to import the a web scraper module
from bs4 import BeautifulSoup

# Need to import the requests module to make a request to the website
import requests

# Need to import the time module to allow the program to sleep
import time

# Need to import the json module to allow the program to write to a json file
import json

# Need to import the os module to allow the program to create a directory
import os


# Create a helper class function to get the data from the website
# Make a request to the website 
response = requests.get(self.url)

# Parse HTML 
soup = BeautifulSoup(response.text, "html.parser")

# Find and extract data
...

# Return the data
return data
class Scraper:
    """A class to scrape data from the website"""

    def __init__(self, url, name):
        self.url = url
        self.name = name

        """A method to get the data from the website"""
        # Make a request to the website
        response = requests.get(self.url)
        # Create a soup object to parse the html
        soup = BeautifulSoup(response.text, "html.parser")
        # Find the table on the website
        table = soup.find("table", {"class": "wikitable sortable"})
        # Find all the rows in the table
        rows = table.find_all("tr")
        # Create a list to store the data
        data = []
        # Loop through the rows
        for row in rows[1:]:
            # Find all the columns in the row
            cols = row.find_all("td")
            # Get the data from the columns
            rank = cols[0].text.strip()
            country = cols[1].text.strip()
            population = cols[2].text.strip()
            # Append the data to the list
            data.append([rank, country, population])
        # Return the data
        return data


test = Scraper(
    "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population",
    "test",
)
