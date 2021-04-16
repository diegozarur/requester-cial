from typing import Text

import requests
from requests import Response

from services.crawler.base_crawler import BaseCrawler


class EnCrawler(BaseCrawler):
    def __init__(self):
        super().__init__()

    def get_page(self, url: Text) -> Response:
        return self._session.get(url)
