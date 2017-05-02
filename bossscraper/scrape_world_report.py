import json
from retrying import retry

from singlepagescraper import ScrapeNetworkPage
from singlepagescraper import ScrapeANSPage

COUNTRY_SKIP_LIST = []

BASE_URL = "http://bgp.he.net"

def export_to_json_file(json_object, file_name):
    """
    (json,str) -> (str)
    Export given json data into the file_name given.
    """
    with open(file_name, 'w') as ex_file:
        json.dump(json_object, ex_file)

@retry
def scrape_pages_for_mapping(data):
    mapping = dict()
    for obj in data:
        if obj not in COUNTRY_SKIP_LIST:
            try:
                ANSPage = ScrapeANSPage(_build_url(obj[1]),"asns",obj[1])
                mapping.update(ANSPage.JSONObj)
            except:
                COUNTRY_SKIP_LIST.append(obj)

    return mapping

def _build_url(countryCode):
    """
    (str) -> (str)
    Takes in countryCode and returns entire URL for country page to scrape
    """
    return BASE_URL + "/country/" + countryCode

#sequence to run scraping across page
homePage = ScrapeNetworkPage(BASE_URL + "/report/world","table_countries")
homePageData = homePage.get_data_from_table()
export_to_json_file(scrape_pages_for_mapping(homePageData), "scrape_results.json")
