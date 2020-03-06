# HTML Parser: https://docs.python.org/3/library/html.parser.html
# Web Scrapper: http://scrapingauthority.com/2016/08/25/web-scraping-beautifulsoup/
# Check on www.website/robots.txt

from collections import deque
from bs4 import BeautifulSoup
from urlparse import urljoin
import sys
import urllib2
from protego import Protego
import requests
from pdb import set_trace


#url = raw_input("Input the url to start the crawling (example: http://www.google.com ):")
url = "http://www.google.com"
queue, visited_links= deque([]), []


def bfs_crawler(url):
    count_limit = 10
    visited_links.append(url)
    if len(queue) > count_limit:
        return

    url_file = urllib2.urlopen(url)
    soup = BeautifulSoup(url_file.read())
    url_list = soup.findAll("a", href=True)

    for link in url_list:
        flag = 0
        # Complete relative URLs and strip trailing slash
        complete_url = urljoin(url, link["href"]).rstrip('/')

        if robot_txt_allowed(link["href"]) is True:
            print ("this link is allowed", link)
        else:
            print("this link is not allowed",link)

        # Check if the URL already exists in the queue
        for j in queue:
            if j == complete_url:
                flag = 1
                break

        # If not found in queue
        if flag == 0:
            if len(queue) > count_limit:
                return
            if (visited_links.count(complete_url)) == 0:
                queue.append(complete_url)

    # Pop one URL from the queue from the left side so that it can be crawled
    current = queue.popleft()
    # Recursive call to crawl until the queue is populated with 100 URLs
    bfs_crawler(current)

def robot_txt_allowed(link):
    try:
        r = requests.get(str(link)+"/robots.txt")
        rp = Protego.parse(r.text)
        return rp.can_fetch(link,"*")
    except:
        return False

def main():

    bfs_crawler(url)
    # Print queue
    for i in queue:
        print i
    for v in visited_links:
        print v

if __name__ == "__main__":
    main()