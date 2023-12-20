# Python
"""
Scraper module provides web scraping functionality using BeautifulSoup.

Contains Scraper base class for scraping pages and parsing HTML.
Subclasses like MemoryAlphaScraper override base class for specific sites.
"""

from bs4 import BeautifulSoup
import urllib.request

MEMORY_ALPHA_BASE_URL = "https://memory-alpha.fandom.com/wiki/"
EX_ASTRIS_SCIENTIA_BASE_URL = "https://www.ex-astris-scientia.org/"


class Scraper:
    """Base class for scraping pages and parsing HTML."""
    
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
        super().__init__(name, MEMORY_ALPHA_BASE_URL)

    def get_aside_section(self):
        """Returns the aside section of the page.
        
        Returns:
            bs4.element.Tag: The <aside> tag object.
            None: If the <aside> tag is not found.
        """
        div = self.soup.find("div", {"class": "mw-parser-output"})
        if div is None:
            print("No div found.")
            return None
        else:
            print("div found.")
        # print all the children and tags of the div
        for child in div.children:
            print(child)
            print(child.name)
        aside = self.soup.find_all("aside")
        if aside is None:
            print("No aside section found.")
            return None
        else:
            print("aside section found.")
            return aside

    def get_table_of_contents(self):
        """Returns the table of contents of the page.

        Returns:
            bs4.element.Tag: The <table> tag object.
            None: If the <table> tag is not found.
        """
        #find the div with the id of "toc"
        toc = self.soup.find("div", {"class": ["toc"]})
        print(toc)
        if toc is not None:
            print("Table of contents found.")
            return toc
        else:
            print("No table of contents found.")
            return None


    def get_main_section(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        main = self.soup.find("div", {"class": ["mw-parser-output"]})
        return main
    

    def test_toc(self):
        """A test summary to get the table of contents from a wiki with a main page"""
        main = self.get_main_section()
        if main is not None:
            print("Main section found.")

        else:
            print("No main section found.")
        toc = self.get_table_of_contents(main)
        if toc is not None:
            print("Table of contents found.")
        else:
            print("No table of contents found.")


    
    @staticmethod
    def format_string(input_string):
        """Format a string by capitalizing first letter of each word and replacing spaces with underscores.

        Args:
            input_string (str): The input string to format.

        Returns:
            str: The formatted string.
        """
        words = input_string.split()
        formatted_words = [word.capitalize() for word in words]
        output_string = "_".join(formatted_words)

        return output_string

dax = MemoryAlphaScraper((MemoryAlphaScraper.format_string("jadzia dax")))
print(dax.name)
# dax.get_aside_section()
# dax.test_toc()
# dax.get_main_section()
# class ExAstrisScientiaScraper(Scraper):

#     """A scraper for the Ex Astris Scientia wiki.
    
#     The Ex Astris Scientia wiki contains information 
#     Series, Ships, Schematics, and Particles.
#     """

#     def __init__(self, name, url):
#         """Initializes an ExAstrisScientiaScraper object.
        
#         Args:
#             name (str): The name to initialize the scraper with.
#             url (str): The base URL of the wiki.
#         """
#         super().__init__(name, url)


#     #NOTE the way the information is parsed on the urls for EAS is different than MA so need to change how the URL is handled for this class
#     @staticmethod
#     def format_url(url):
#         """_summary_

#         Example:
#             url = "https://www.ex-astris-scientia.org/"
#             formated_url = "https://www.ex-astris-scientia.org/episodes/<tng1>.htm

#             url = "https://www.ex-astris-scientia.org/"
#             formated_url = "https://www.ex-astris-scientia.org/database/particles1.htm#a
#         Args:
#             url (_type_): _description_
#         """

