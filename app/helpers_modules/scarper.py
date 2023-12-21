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
        url = f"{self.base_url}{self.name}"
        try:
            html_content = urllib.request.urlopen(url)
            soup = BeautifulSoup(html_content, "html.parser")
            print(url)
            return soup
        except urllib.error.HTTPError as e:
            print(e)
            return None
         
    @staticmethod
    def format_string(string):
        """Correctly formats a string to be used in a URL.
        
        Args:
            string (str): The string to format.
            
        Returns:
            str: The formatted string.
        """
        return string


class MemoryAlphaScraperModule(Scraper):
    """A scraper for the Memory Alpha wiki."""
    
    def __init__(self, name):
        """Initializes a MemoryAlphaScraper object.
        
        Args:
            name (str): The name to initialize the scraper with.
        """
        super().__init__(name, MEMORY_ALPHA_BASE_URL)
        self.main = self.get_main_section()

    def get_aside_section(self):
        """Returns the aside section of the page.
        
        Returns:
            bs4.element.Tag: The <aside> tag object.
            None: If the <aside> tag is not found.
        """
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
        toc = self.soup.find_all("div", {"class": "toc"})
        if toc is not None:
            print("toc found.")
            levels = self.soup.find_all('li', class_="toclevel-1")
            if levels is not None:
                print("toc levels found.")
                for level in levels:
                    print(level.get_text())
            else:
                print("No toc levels found.")
                return None
            return "toc found"
        else:
            print("No toc found.")
            return None
        
    def get_main_section(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        main = self.soup.find("div", {"id": ["mw-parser-output"]})
        return main
    


# dax = MemoryAlphaScraperModule((MemoryAlphaScraperModule.format_string("jadzia dax")))
# print(dax.name)
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

