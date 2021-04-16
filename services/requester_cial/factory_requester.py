from abc import ABCMeta, abstractmethod
from typing import Dict, List

from services.requester_cial.requester import Requester


class RequesterFactory(metaclass=ABCMeta):

    def get_requester(self, websites: List):
        try:
            requester: Requester = self._create_requester()
            return requester.extract_data_from_site(websites)
        except Exception as e:
            raise e

    @abstractmethod
    def _create_requester(self) -> Requester:
        ...
