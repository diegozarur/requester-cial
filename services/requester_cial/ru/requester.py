from typing import List

from services.requester_cial.ru.crawler import RuCrawler
from services.requester_cial.ru.scraper import RuScraper
from services.requester_cial.requester import Requester


class RuRequester(Requester):
    def __init__(self, crawler: RuCrawler, scraper: RuScraper):
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
