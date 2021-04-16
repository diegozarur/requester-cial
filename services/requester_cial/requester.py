from abc import ABCMeta, abstractmethod
from typing import Dict, List


class Requester(metaclass=ABCMeta):
    @abstractmethod
    def extract_data_from_site(self, sites: List) -> List:
        ...
