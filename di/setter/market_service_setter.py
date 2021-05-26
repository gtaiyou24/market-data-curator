from injector import Module, Binder, singleton

from domain.model.market.market_service import MarketService
from port.adapter.service.market import MarketServiceImpl


class MarketServiceSetter(Module):

    def configure(self, binder: Binder) -> None:
        binder.bind(MarketService, to=MarketServiceImpl, scope=singleton)
