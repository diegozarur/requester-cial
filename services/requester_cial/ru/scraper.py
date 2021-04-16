import re
from typing import Text, List
import phonenumbers as pn
from services.scrapper.base_scrapper import BaseScrapper


class RuScraper(BaseScrapper):
    """
    Create a scraper to find phone numbers and logos
    """

    def __init__(self):
        super().__init__()
        self.__region = "RU"

    def get_logo_url(self, domain: Text) -> Text:

        logo_link = self._html_parsed.find('img', {'class': re.compile(r'logo')})
        if not logo_link:
            all_images_from_site = self._html_parsed.find_all("img")
            img_url = self._find_logo_in_attr_src(all_images_from_site)
        else:
            img_url = logo_link['src']

        return self._get_correct_logo_url(domain, img_url)

    def get_phone_numbers(self, text) -> List:
        return [pn.format_number(match.number, pn.PhoneNumberFormat.INTERNATIONAL).replace('-', ' ') for match in
                pn.PhoneNumberMatcher(text, self.__region)]
