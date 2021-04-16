from services.logo_type.factory_logo_type import LogoTypeFactory
from services.logo_type.logo_type import LogoType
from services.logo_type.types.logo_with_path.type import LogoWithPath


class LogoWithpathFactory(LogoTypeFactory):
    def _create_logo_type(self) -> LogoType:
        return LogoWithPath()
