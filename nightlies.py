import feedparser
from BeautifulSoup import BeautifulSoup
import urllib
import anydbm
import time

def list_nightlies(initial=False):
    if initial:
        return scraper()
    url = "http://haiku-files.org/vmware/rss/"
    d = feedparser.parse(url)
    return set(x.title.split('-')[2] for x in d.entries)

def scraper():
    url = "http://haiku-files.org/vmware/index.php?show=all"
    soup = BeautifulSoup(urllib.urlopen(url))
    return set(sorted((x.text.split('-')[2] for x in soup.findAll('a', 'link') if x.text[0] == 'h'), reverse=True))

def get_db():
     return anydbm.open('nighties', 'c')
def store():
    db = get_db()
    if 'meta' in db:
        for rev in list_nightlies():
            if str(rev) not in db:
                db[str(rev)] = 'unknown'
    else:
        for rev in scraper():
            db[str(rev)] = 'unknown'
        db['meta'] = 'setup'
    db['last-edit'] = time.ctime() +' '+ time.strftime('%Z')
        
if __name__ == '__main__':
    import sys
    if sys.argv > 1:
        if sys.argv[1].lower() in ['-d', 'db', 'database']:
            store()
    else:
        print list_nightlies()