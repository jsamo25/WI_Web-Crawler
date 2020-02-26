# HTML Parser: https://docs.python.org/3/library/html.parser.html
# Web Scrapper: http://scrapingauthority.com/2016/08/25/web-scraping-beautifulsoup/
# Check on www.website/robots.txt


from bs4 import BeautifulSoup
from pdb import set_trace

with open ("index.html", "r") as f:
    contents = f.read()
    soup = BeautifulSoup(contents, "lxml")

    for tag in soup.find_all("li"):
        print("{0}: {1}".format(tag.name, tag.text))

#following tutorial from: http://zetcode.com/python/beautifulsoup/