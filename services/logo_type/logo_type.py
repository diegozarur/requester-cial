from abc import ABCMeta, abstractmethod
from typing import Text


class LogoType(metaclass=ABCMeta):

    @abstractmethod
    def get_logo(self, domain: Text, logo_url: Text) -> Text:
        ...
