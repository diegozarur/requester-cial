from typing import Text, List, Dict

from services.requester_cial.en.crawler import EnCrawler
from services.requester_cial.en.scraper import EnScraper
from services.requester_cial.requester import Requester


class EnRequester(Requester):
    def __init__(self, crawler: EnCrawler, scraper: EnScraper):
        self.__crawler = crawler
        self.__scraper = scraper

    def extract_data_from_site(self, sites: List) -> List:
        result = []
        for site in sites:
            response = self.__crawler.get_page(site.get('site'))
            self.__scraper.html_parsed = response.text

            data_extracted = {
                'logo': self.__scraper.get_logo_url(site.get('domain')),
                'phones': self.__scraper.get_phone_numbers(response.text),
                'website': site.get('site')
            }
            result.append(data_extracted)
        return result
