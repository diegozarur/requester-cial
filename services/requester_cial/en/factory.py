from services.requester_cial.en.crawler import EnCrawler
from services.requester_cial.en.requester import EnRequester
from services.requester_cial.en.scraper import EnScraper
from services.requester_cial.factory_requester import RequesterFactory
from services.requester_cial.requester import Requester


class EnRequesterFactory(RequesterFactory):
    def _create_requester(self) -> Requester:
        crawler = EnCrawler()
        scraper = EnScraper()
        return EnRequester(crawler, scraper)
