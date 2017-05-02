import pytest

import singlepagescraper
from singlepagescraper import ScrapeNetworkPage
from singlepagescraper import ScrapeANSPage

ANS_LINE = 'AS11816'
COUNTRY_URL = "http://bgp.he.net/country/"
ET_JSON_RESULT = {'24757': {'Routes v4': '112', 'Routes v6': '0', 'Country': 'ET', 'Name': 'ISP in Ethiopia'}}
ET_DATA_RESULT = [['AS24757', 'ISP in Ethiopia', '3', '112', '0', '0']]

def test_clean_ans():
    assert singlepagescraper.clean_ans(ANS_LINE) == '11816'

def test_scrape_network_page():
    snp = ScrapeNetworkPage(COUNTRY_URL + "ET","asns")
    assert snp.data == ET_DATA_RESULT

def test_scrape_ans_page():
    ans = ScrapeANSPage(COUNTRY_URL + "ET","asns","ET")
    assert ans.JSONObj == ET_JSON_RESULT
