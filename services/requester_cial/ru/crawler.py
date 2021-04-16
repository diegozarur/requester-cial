from typing import Text
from requests import Response

from services.crawler.base_crawler import BaseCrawler


class RuCrawler(BaseCrawler):
    def __init__(self):
        super().__init__()

    def get_page(self, url: Text) -> Response:
        return self._session.get(url)
