import re
from typing import Text, List

from services.scrapper.base_scrapper import BaseScrapper


class EnScraper(BaseScrapper):
    """
    Create a scraper to find phone numbers and logos
    """

    def get_logo_url(self, domain: Text) -> Text:

        logo_link = self._html_parsed.find('img', {'class': re.compile(r'logo')})
        if not logo_link:
            all_images_from_site = self._html_parsed.find_all("img")
            img_url = self._find_logo_in_attr_src(all_images_from_site)
        else:
            img_url = logo_link['src']

        return self._get_correct_logo_url(domain, img_url)

    def get_phone_numbers(self, text) -> List:
        phone_numbers = [phone.replace('-', ' ') for phone in re.findall(r'\+[-()\s\d]+?(?=\s*[+<])', text)]
        if not phone_numbers:
            phone_regex = re.compile(r'''(
                (\(\d{3}\))? # area code
                (\s| |\.)? # separator
                (\d{3}) # first 3 digits
                (\s|-|\.) # separator
                (\d{4}) # last 4 digits
                (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
                )''', re.VERBOSE)
            match_numbers = phone_regex.findall(text)
            phone_numbers = [match[0] for match in match_numbers]

        return phone_numbers
