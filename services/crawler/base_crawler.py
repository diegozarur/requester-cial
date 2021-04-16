from typing import Text

import requests
from abc import ABCMeta, abstractmethod

from requests import Response


class BaseCrawler(metaclass=ABCMeta):
    def __init__(self):
        self._session = requests.Session()

    @abstractmethod
    def get_page(self, url: Text) -> Response:
        ...
