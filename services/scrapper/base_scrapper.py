import re
from abc import ABCMeta, abstractmethod
from typing import Text, List

from bs4 import BeautifulSoup

from services.logo_type.selector import LogoTypeSelector


class BaseScrapper(metaclass=ABCMeta):
    def __init__(self):
        self._html_parsed: BeautifulSoup
        self.__logo_selector = LogoTypeSelector()

    @property
    def html_parsed(self):
        return self._html_parsed

    @html_parsed.setter
    def html_parsed(self, value):
        self._html_parsed = BeautifulSoup(value, 'html.parser')

    @abstractmethod
    def get_logo_url(self, domain: Text) -> Text:
        ...

    @abstractmethod
    def get_phone_numbers(self, text) -> List:
        ...

    def _find_logo_in_attr_src(self, all_images_from_site) -> Text:
        logo: Text = ''
        for tag_img in all_images_from_site:
            match = re.search(r'logo', tag_img['src'], flags=re.IGNORECASE)
            if match:
                logo = tag_img['src']
                break
        return logo

    def _get_correct_logo_url(self, domain: Text, img_url: Text) -> Text:
        selector = self.__logo_selector.select_logo_type(img_url)
        if selector:
            return selector.complete_url_logo(domain=domain, logo_url=img_url)
        return ''
