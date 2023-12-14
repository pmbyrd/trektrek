# Python
"""
Scraper module provides web scraping functionality using BeautifulSoup.

Contains Scraper base class for scraping pages and parsing HTML.
Subclasses like MemoryAlphaScraper override base class for specific sites.
"""

from bs4 import BeautifulSoup
import urllib.request

STAPI_BASE_URL = "https://memory-alpha.fandom.com/wiki/"
EX_ASTRIS_SCIENTIA_URL = "https://www.ex-astris-scientia.org/"


class Scraper:

    def __init__(self, name, base_url):
        """Initializes a Scraper object.

        Args:
            name (str): Name of the character or object to be scraped. 
            base_url (str): Link to the wiki page for the character or object.
        """
        self.name = name
        self.base_url = base_url
        self.soup = self.get_soup()

    def __repr__(self):
        return f"<Scraper name={self.name} base_url={self.base_url}>"

    def get_soup(self):
        """Returns a BeautifulSoup object for the given name and base_url.
        
        Parses the HTML of the page and returns a BeautifulSoup object.

        Returns:
            bs4.BeautifulSoup: A BeautifulSoup object.
        """
        with urllib.request.urlopen(self.base_url) as response:
            html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        return soup

    def make_pretty_soup(self):
        """Returns a prettified BeautifulSoup object for the given name and base_url.
        
        Returns:
            bs4.BeautifulSoup: A nested BeautifulSoup object. That is, the object is a 
            BeautifulSoup object that contains another BeautifulSoup object. Creates a 
            navigational structure for parsing the HTML.
        """
        return BeautifulSoup(self.soup.prettify(), 'html.parser')
    
    def get_all_links(self):
        """Returns a list of all links on the page.
        
        Returns:
            list: A list of all links on the page.
            
        Raises:
            urllib.error.HTTPError: If the page is not found.
            
        Returns:
            None: If no links are found.
        """
        links = []
        try:
            for link in self.soup.find_all('a'):
                links.append(link.get('href'))
        except urllib.error.HTTPError as e:
            print(e)
            return None
        if len(links) < 1:
            return None
        else:
            return links
        
    @staticmethod
    def format_string(string):
        """Correctly formats a string to be used in a URL.
        
        Args:
            string (str): The string to format.
            
        Returns:
            str: The formatted string.
        """
        return string


class MemoryAlphaScraper(Scraper):
    """A scraper for the Memory Alpha wiki."""
    
    def __init__(self, name):
        """Initializes a MemoryAlphaScraper object.
        
        Args:
            name (str): The name to initialize the scraper with.
        """
        super().__init__(name, STAPI_BASE_URL)

    def get_aside_section(self):
        """Returns the aside section of the page.
        
        Returns:
            bs4.element.Tag: The <aside> tag object.
        """
        return self.soup.find("aside")

    
    @staticmethod
    def format_string(string):
        """Format a string to capitalize first letter of each word and replace spaces with underscores.

        Args:
            string (str): The input string to format.

        Returns:
            str: The formatted string.
        """

        words = string.split()

        for i in range(len(words)):
            words[i] = words[i].capitalize()
    
        string = "_".join(words)

        return string
    

class ExAstrisScientiaScraper(Scraper):
    """A scraper for the Ex Astris Scientia wiki.
    
    The Ex Astris Scientia wiki contains information 
    Series, Ships, Schematics, and Particles.
    """

    def __init__(self, name, url):
        """Initializes an ExAstrisScientiaScraper object.
        
        Args:
            name (str): The name to initialize the scraper with.
            url (str): The base URL of the wiki.
        """
        super().__init__(name, url)


    #NOTE the way the information is parsed on the urls for EAS is different than MA so need to change how the URL is handled for this class
    @staticmethod
    def format_url(url):
        """_summary_

        Example:
            url = "https://www.ex-astris-scientia.org/"
            formated_url = "https://www.ex-astris-scientia.org/episodes/<tng1>.htm

            url = "https://www.ex-astris-scientia.org/"
            formated_url = "https://www.ex-astris-scientia.org/database/particles1.htm#a
        Args:
            url (_type_): _description_
        """


Pike = MemoryAlphaScraper.format_string("christorpher pike")
print(Pike)
#Create an instance of a Pike object
Pike = MemoryAlphaScraper(Pike)
Pike.name
Pike.get_all_links()
#Print only the first ten links
print_all_links(Pike).len(10)