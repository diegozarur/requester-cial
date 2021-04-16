from services.requester_cial.ru.crawler import RuCrawler
from services.requester_cial.ru.requester import RuRequester
from services.requester_cial.ru.scraper import RuScraper
from services.requester_cial.factory_requester import RequesterFactory
from services.requester_cial.requester import Requester


class RuRequesterFactory(RequesterFactory):
    def _create_requester(self) -> Requester:
        crawler = RuCrawler()
        scraper = RuScraper()
        return RuRequester(crawler, scraper)
