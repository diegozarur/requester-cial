from services.requester_cial.en.factory import EnRequesterFactory
from services.requester_cial.factory_requester import RequesterFactory
from services.requester_cial.ru.factory import RuRequesterFactory


class RequesterSelector():
    __REQUESTER_FACTORIES = {
        'com': EnRequesterFactory(),
        'com.au': EnRequesterFactory(),
        'ru': RuRequesterFactory()
    }

    def get_requester_factory(self, requester_type: str) -> RequesterFactory:
        if requester_type not in self.__REQUESTER_FACTORIES:
            raise ValueError("Requester not found.")
        else:
            return self.__REQUESTER_FACTORIES[requester_type]
