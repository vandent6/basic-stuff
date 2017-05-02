import requests
from bs4 import BeautifulSoup
from retrying import retry

HEADERS = {
            'Cache-Control': "no-cache",
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, sdch, br',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
          }

def make_request(url):
    """
    (str) -> (request obj)
    Takes url and makes a call using requests class.
    Returns the request object.
    """
    request = requests.request("GET",
                                url,
                                timeout=30,
                                headers=HEADERS)
    
    return request


class BaseScraper:
    def __init__(self, pageURL):
        self.pageSoup = self.__get_soup(pageURL)
    
    def __get_soup(self, pageURL):
        return BeautifulSoup(make_request(pageURL).content, "lxml")

class ArticleHandler:
    def __init__(self, ArticleSoup):
        self.ArticleSoup = ArticleSoup
        self.Title = self.get_article_title()
        self.HREF = self.get_article_href()
        
    def get_article_title(self):
        if self.ArticleSoup.a: 
            return self.ArticleSoup.a.text.replace("\n", " ").strip()
        else: 
            return self.ArticleSoup.contents[0].strip()

    def get_article_href(self):
        if self.ArticleSoup.a:
            return self.ArticleSoup.find('a').get('href')
        else:
            return "no href"

'''       
URL = 'https://www.nytimes.com'
hi = BaseScraper(URL)
soup = hi.pageSoup

articles = []

for title in soup.find_all(class_='story-heading'):
    articles.append(ArticleHandler(title))


for art in articles:
    print(art.Title)
    print(art.HREF)
'''
