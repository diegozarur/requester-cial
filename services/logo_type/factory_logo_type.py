from abc import ABCMeta, abstractmethod
from typing import Text

from services.logo_type.logo_type import LogoType


class LogoTypeFactory(metaclass=ABCMeta):
    def complete_url_logo(self, domain: Text, logo_url: Text) -> Text:
        logo_type: LogoType = self._create_logo_type()
        return logo_type.get_logo(domain, logo_url)

    @abstractmethod
    def _create_logo_type(self) -> LogoType:
        ...
