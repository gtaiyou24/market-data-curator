from typing import Type

from injector import Injector, T

from di.setter import MarketServiceSetter, MarketAdapterSetter, MarketTradesRepositorySetter


class DIManager:

    def __init__(self):
        self.__injector = Injector([
            MarketAdapterSetter(),
            MarketServiceSetter(),
            MarketTradesRepositorySetter()
        ])

    def get(self, abstract_class: Type[T]) -> T:
        return self.__injector.get(abstract_class)
