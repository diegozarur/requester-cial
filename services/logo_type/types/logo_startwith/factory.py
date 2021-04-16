from services.logo_type.factory_logo_type import LogoTypeFactory
from services.logo_type.logo_type import LogoType
from services.logo_type.types.logo_startwith.type import LogoTypeStartWith


class LogoStartWithFactory(LogoTypeFactory):
    def _create_logo_type(self) -> LogoType:
        return LogoTypeStartWith()
