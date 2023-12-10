import logging
import requests
from logging.handlers import RotatingFileHandler
import urllib.request
from bs4 import BeautifulSoup as Soup
from app.extensions import db
from flask.logging import default_handler
from random import randint


# ***************** Helper Datatypes *****************
color_hex_values = [
    "#ffaa00",
    "#552255",
    "#663366",
    "#774477",
    "#885588",
    "#996699",
    "#ff8800",
    "#d0b0a0",
    "#bbbbff",
    "#99aa66",
    "#00bb00",
    "#33ff33",
    "#ddffdd",
    "#ffebde",
    "#cc99cc",
    "#f6eef6",
    "#aa66aa",
    "#dd88dd",
]

        print(soup)

def get_random_color():
    color = color_hex_values[randint(0, len(color_hex_values) - 1)]
    return color


def configure_logging(app):
    # Logging Configuration
    if app.config["LOG_WITH_GUNICORN"]:
        gunicorn_error_logger = logging.getLogger("gunicorn.error")
        app.logger.handlers.extend(gunicorn_error_logger.handlers)
        app.logger.setLevel(logging.DEBUG)
    else:
        file_handler = RotatingFileHandler(
            "instance/trektrek.log", maxBytes=16384, backupCount=20
        )
        file_formatter = logging.Formatter(
            "%(asctime)s %(levelname)s %(threadName)s-%(thread)d: %(message)s [in %(filename)s:%(lineno)d]"
        )
        file_handler.setFormatter(file_formatter)
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

    # Remove the default logger configured by Flask
    app.logger.removeHandler(default_handler)

    app.logger.info("Starting the TrekTrek App...")


def connect_db(app):
    """Connect this database to provided Flask app.
    You should call this in your Flask app.
    """
    db.app = app
    db.init_app(app)


def replace_space(string):
    """A helper function that replaces spaces with underscores"""
    if " " in string:
        string = string.replace(" ", "_")
        return string
    else:
        return string


# ***************** Class helper functions *****************
class MemoryAlphaScraper:
    def __init__(self, name, base_url="https://memory-alpha.fandom.com/wiki"):
        self.base_url = base_url
        self.name = name

    def soup(self):
        url = f"{self.base_url}/{self.name}"
        try:
            html_content = urllib.request.urlopen(url)
            soup = Soup(html_content, "html.parser")
            print(url)
            return soup
        except urllib.error.HTTPError as e:
            print(e)
            return None

    def get_summary(self):
        """Gets the summary of the show"""
        soup = self.soup()
        div = soup.find("div", {"class": "mw-parser-output"})
        content_nodes = div.find_all(["h2", "h3", "p", "b", "ul", "span"])
        # Create a list to store tuples of paired elements (headline, content)
        spans = div.find_all("span", class_="mw-headline")
        headlines = div.find_all(["h2", "h3", "h4"])
        content_nodes = div.find_all(["p", "b", "ul"])

        paired_elements = []
        current_headline = None

        for node in content_nodes:
            if node.name in ["h2", "h3", "h4"]:
                # If the node is a headline, update the current_headline
                current_headline = node.get_text()
            else:
                # If the node is not a headline, it's content associated with the current_headline
                paired_elements.append((current_headline, node.get_text()))

        for span in spans:
            if span.name in ["span"]:
                # If the node is a headline, update the current_headline
                current_headline = span.get_text()

        # Loop through the paired elements and print the information
        for headline, content in paired_elements:
            print(headline)
            print(content)
            print(spans)
            return paired_elements
