from typing import List
import multiprocessing as mp
import itertools
from operator import itemgetter
from concurrent.futures import ThreadPoolExecutor, as_completed

import tldextract

from services.custom_file_open import CustomFileOpen
from services.requester_cial.factory_requester import RequesterFactory
from services.requester_cial.requester_selector import RequesterSelector
from services.loggers import logger


class RequesterService:
    def __init__(self):
        self.__requester_factory_selector = RequesterSelector()

    @logger.log_error()
    def extract(self) -> List:

        websites = self.__get_websites_and_grouped()
        return self.__execute_in_concurrently(websites)

    def __execute_in_concurrently(self, websites: List) -> List:
        """
        Args:
            websites (List):
        """
        processes = []
        results = []
        with ThreadPoolExecutor(max_workers=mp.cpu_count()) as executor:
            for url in websites:
                processes.append(executor.submit(self.__find_requester_and_get_results, url))

        for task in as_completed(processes):
            results.extend(task.result())
        return results

    def __find_requester_and_get_results(self, websites_group: dict):
        """
        Args:
            websites_group (dict):
        """
        requester_factory: RequesterFactory = self.__requester_factory_selector.get_requester_factory(
            websites_group.get('type'))
        return requester_factory.get_requester(websites_group.get('sites'))

    def __get_websites_and_grouped(self):
        custom_file_open = CustomFileOpen()
        websites = custom_file_open.get_content_in_list()
        return self.__group_websites(self.__create_detail_list_of_websites(websites))

    def __group_websites(self, websites: List) -> List:
        """
        Args:
            websites (List):
        """
        sites_grouped_by_suffix = []
        websites_ordered = sorted(websites, key=itemgetter('suffix'))
        for key, group in itertools.groupby(websites_ordered, key=itemgetter('suffix')):
            sites_grouped_by_suffix.append({'type': key, 'sites': list(group)})

        return sites_grouped_by_suffix

    def __create_detail_list_of_websites(self, websites: List):
        """
        Args:
            websites (List):
        """
        data = []
        for site in websites:
            ext = tldextract.extract(site)
            data.append({
                'site': site,
                'suffix': ext.suffix,
                'domain': ext.fqdn
            })
        return data
