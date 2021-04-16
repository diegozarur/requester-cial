from typing import Text

from services.logo_type.logo_type import LogoType


class LogoWithHttps(LogoType):
    def get_logo(self, domain: Text, logo_url: Text) -> Text:
        return logo_url
