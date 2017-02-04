import urllib.request
from bs4 import BeautifulSoup
from time import sleep
import frogress

PAGEPATH = 'https://cdxnodengn.epa.gov'

def get_html(url):
    with urllib.request.urlopen(url) as response:
        return response.read()

def get_links(html):

    soup = BeautifulSoup(html)

    all_links = [link['href'] for link in soup.findAll('a', href=True) if 'download' in link['href']]

    return all_links

def get_allllll_the_things():

    pagenum = 1
    while pagenum < 735:
        url = 'https://cdxnodengn.epa.gov/cdx-enepa-II/public/action/eis/search/search;jsessionid=E6799FC1327C75228EF83107EDEE25C2?searchCriteria.endCommentLetterDate=&d-446779-p={pagenum}&searchCriteria.title=&searchRecords=Search&searchCritera.primaryStates=&searchCriteria.endFRDate=&searchCriteria.startCommentLetterDate=&searchCriteria.startFRDate=#results'.format(pagenum = pagenum)

        pagenum += 1
        links = get_links(get_html(url))

        yield links

if __name__ == "__main__":

    links_file = 'paths.txt';
    domain_file = 'url.txt';

    for linkset in frogress.bar(get_allllll_the_things()):
        with open(links_file, 'a') as lf:
            lf.write("\n".join(linkset))
        sleep(0.2)
