from typing import Text

from services.logo_type.logo_type import LogoType
from services.logo_type.types.logo_startwith.factory import LogoStartWithFactory
from services.logo_type.types.logo_with_https.factory import LogoWithHttpsFactory
from services.logo_type.types.logo_with_path.factory import LogoWithpathFactory


class LogoTypeSelector:
    """
        Select type of logo use
    """

    def select_logo_type(self, logo_url: Text):

        if not self.__is_empty(logo_url):
            if logo_url.startswith("//"):
                return LogoStartWithFactory()
            if "https" in logo_url:
                return LogoWithHttpsFactory()
            return LogoWithpathFactory()

        return ''

    def __is_empty(self, logo_url) -> bool:
        if logo_url:
            return False
        return True
