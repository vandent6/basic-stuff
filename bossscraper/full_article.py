from scrape_nyt import BaseScraper

def get_article_header(soup):
    return soup.article.header.h1.text

def get_article_synopsis(soup):
    return soup.article.header.div.text

def get_article_content(soup):
    article = ""
    for sec in soup.article.find_all('p'):
        article += str(sec.text)
    return article

def read_from_file(read_file):
    with open(read_file, 'r') as open_file:
        line = open_file.readline()
        while line:
            print(line)
            line = open_file.readline()

URL = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"
scraper = BaseScraper(URL)
soup = scraper.pageSoup


with open('save_file.txt', 'w') as open_file:
    open_file.write(get_article_content(soup))
