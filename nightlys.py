import feedparser
from BeautifulSoup import BeautifulSoup
import urllib

def list_nightlies(initial=False):
    if initial:
        return scraper()
    url = "http://haiku-files.org/vmware/rss/"
    d = feedparser.parse(url)
    return set(x.title.split('-')[2] for x in d.entries)

def scraper():
    url = "http://haiku-files.org/vmware/index.php?show=all"
    soup = BeautifulSoup(urllib.urlopen(url))
    return set(x.text.split('-')[2] for x in soup.findAll('a', 'link') if x.text[0] == 'h')
    
if __name__ == '__main__':
    print list_nightlies()