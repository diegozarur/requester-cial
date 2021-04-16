from services.logo_type.factory_logo_type import LogoTypeFactory
from services.logo_type.logo_type import LogoType
from services.logo_type.types.logo_with_https.type import LogoWithHttps


class LogoWithHttpsFactory(LogoTypeFactory):
    def _create_logo_type(self) -> LogoType:
        return LogoWithHttps()
