import json
import requests
from bs4 import BeautifulSoup
from retrying import retry

HEADERS = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, sdch, br',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
          }

ROW_SKIP_LIST = []

def clean_ans(ans):
    """
    (str) -> (str)
    Removes prefix from the ANS string and returns result.
    """
    return ans[2:]

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

class ScrapeNetworkPage:
    """
    Class that will scrape the tableID on the pageURL given
    """
    def __init__(self, pageURL, tableID):
        self.tableBody = self.__get_table_body(self.__get_soup(pageURL),
                                               {'id': tableID})
        self.data = self.get_data_from_table()

    def get_data_from_table(self):
        tableData = []
        for row in self.tableBody.find_all('tr'):
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            tableData.append([ele for ele in cols if ele])

        return tableData

    def __get_soup(self, pageURL):
        return BeautifulSoup(make_request(pageURL).content, "lxml")

    def __get_table_body(self, soup, attributes):
        return soup.find('table', attrs=attributes).find('tbody')

class ScrapeANSPage(ScrapeNetworkPage):
    """
    Uses ScrapeNetworkPage but has unique json builder
    """
    def __init__(self, pageURL, tableID, countryCode):
        super(ScrapeANSPage, self).__init__(pageURL, tableID)
        self.countryCode = countryCode
        self.Errors = []
        self.JSONObj = self.get_json_from_data(self.data)

    @retry
    def get_json_from_data(self, data):
        json_obj = dict()
        for obj in data:
            if obj not in ROW_SKIP_LIST:
                try:
                    json_obj[clean_ans(obj[0])] = self.__get_json_from_row(obj)
                except:
                    ROW_SKIP_LIST.append(obj)

        return json_obj

    def __get_json_from_row(self, row):
        return {
                "Country" : self.countryCode,
                "Name": row[1],
                "Routes v4": row[3],
                "Routes v6": row[5]
                }
