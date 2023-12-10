# Python
"""
A module to scrape the web for data.
Imports the BeautifulSoup library. 
Imports the requests library. 
"""
from bs4 import BeautifulSoup
import urllib.request

STAPI_BASE_URL = "https://memory-alpha.fandom.com/wiki/"

class Scraper:
    """A Base class for creating a web scraper
    Uses BeautifulSoup to parse the website and requests to make the request.
    Other scrapers will inherit from this class.
    url: (String) The url of the website to scrape
    parser: (BeautifulSoup)The parser to use when scraping the website (defaults to html.parser)
    name: (String) The name of the Scraper
    soup: (BeautifulSoup) The soup object created from the website
    """# Make a request to the website
    def __init__(self, name, base_url): 
        """Initialize the Scraper class
        name: (String) The name of the Scraper
        url: (String) The url of the website to scrape
        Returns: (Scraper) A Scraper object
        """
        self.name = name
        self.base_url = base_url
        self.soup = self.soup()
    
    def __repr__(self):
        return f"{self.name}"

    def soup(self):
        """create a soup object from the website
        uses its own url attribute and the name attribute to create the soup object
        returns: (beautifulsoup) the soup object created from the website
        returns: none if there is an httperror
        returns none if there is a urlerror
        """
        # make a request to the website
        url = f"{self.base_url}/{self.name}"
        try:
            html_content = urllib.request.urlopen(url)
            soup = BeautifulSoup(html_content, 'html.parser')
            return soup
            # fix need to add more error handling
        except urllib.error.httperror as e:
            print(e)
            return None


    #Write a function parses the website and returns the summary
    def get_main(self):
        """Gets the summary of the webpage

        Takes it's own attibutes to begin parsing the webpage
        """
        #if the div has the class of main than parse it's contents.
        main = self.soup
        print(main)


