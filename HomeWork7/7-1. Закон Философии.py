import time
import argparse
from urllib import urlopen
from urllib.parse import urlparse

from bs4 import BeautifulSoup

SEARCH_HEADER = "философия"


class ParsedPage:
    def __init__(self, header, first_href):
        self._header = header
        self._first_href = first_href

    def get_header(self):
        return self._header

    def get_first_href(self):
        return self._first_href


def isValid(ref, paragraph):
    if not ref or "#" in ref or "//" in ref or ":" in ref:
        return False
    if "/wiki/" not in ref:
        return False
    if ref not in paragraph:
        return False
    prefix = paragraph.split(ref, 1)[0]
    if prefix.count("(") != prefix.count(")"):
        return False
    return True


def validateTag(tag):
    name = tag.name
    isParagraph = name == "p"
    isList = name == "ul"
    return isParagraph or isList


def parse_url(url_):
    # page = urllib.request.urlopen(url_).read()
    # soup = BeautifulSoup(page, "lxml").find('div', id='mw-content-text')
    page = urllib.urlopen(url_)
    soup = BeautifulSoup(page.read(), fromEncoding="utf-8")
    for paragraph in soup.find_all(validateTag, recursive=False):
        for link in paragraph.find_all("a"):
            ref = link.get("href")
            if isValid(str(ref), str(paragraph)):
                return ParsedPage(BeautifulSoup(page, "lxml").find('h1', id='firstHeading').get_text(), str(ref))


visited_hrefs = []

parser = argparse.ArgumentParser(description='Problem 7.1')
parser.add_argument("url", type=str, help="wiki url for parsing")
args = parser.parse_args()

url = args.url
base_url = "{0.scheme}://{0.netloc}".format(urlparse(url))

while True:
    parsedPage = parse_url(url)
    print("Going to check: " + url)
    print("Page title: " + parsedPage.get_header())
    if parsedPage.get_first_href() in visited_hrefs:
        print("Cycle detected! Going to shutdown....")
        break
    else:
        if SEARCH_HEADER == parsedPage.get_header().lower():
            print("Search header detected! Well done!")
            break
        else:
            url = base_url + parsedPage.get_first_href()
            visited_hrefs.append(parsedPage.get_first_href())
    time.sleep(2)
