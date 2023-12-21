import logging
from typing import Generator

from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)


class MemoryAlphaScraper:

    def __init__(self, html: str, selectors: dict = None) -> None:
        self.soup = BeautifulSoup(html, 'html.parser')
        self.selectors = selectors or self.default_selectors

    def extract_aside(self) -> BeautifulSoup:
        """Extract the <aside> section from the page."""
        aside = self.soup.select_one(self.selectors['aside'])
        if aside is None:
            logger.warning('Aside section not found')
            return None
        return aside

    def extract_toc(self) -> Generator[dict, None, None]:
        """Extract the table of contents links."""
        toc = self.soup.select_one(self.selectors['toc'])
        if toc is None:
            logger.warning('TOC section not found')
            return
        
        for link in toc.select(self.selectors['toc_link']):
            href = link.get('href')
            text = link.text
            yield {'href': href, 'text': text}

    def extract_main_content(self) -> BeautifulSoup:
        """Extract the main content div."""
        main = self.soup.select_one(self.selectors['main'])
        if main is None:
            logger.error('Main content not found')
            raise Exception('Could not find main content')
        return main

    # Configurable default selectors
    default_selectors = {
        'aside': 'aside',
        'toc': '#toc',
        'toc_link': 'a',
        'main': '.mw-parser-output',
        'img': 'img',
        'img_alt': 'img[alt]',
        'img_src': 'img[src]',
        'img_title': 'img[title]',
        'wiki': 'a[href^="https://memory-alpha.fandom.com/wiki/"]',
    }

dax = MemoryAlphaScraper("https://memory-alpha.fandom.com/wiki/Jadzia_Dax")
print(dax.extract_toc())
import pdb;pdb.set_trace()
