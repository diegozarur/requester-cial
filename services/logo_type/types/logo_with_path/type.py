from typing import Text

from services.logo_type.logo_type import LogoType


class LogoWithPath(LogoType):
    def get_logo(self, domain: Text, logo_url: Text) -> Text:
        return f"https://{domain}{logo_url}"
