from injector import Module, Binder, singleton

from di import Profile, DISwitcher
from domain.model.trade import MarketTradesRepository
from port.adapter.standalone.inmemory import InMemoryMarketTradesRepository


class MarketTradesRepositorySetter(Module):
    INTERFACES = {
        Profile({"inmemory"}): InMemoryMarketTradesRepository
    }

    def configure(self, binder: Binder) -> None:
        binder.bind(MarketTradesRepository, to=DISwitcher.get(self.INTERFACES), scope=singleton)
