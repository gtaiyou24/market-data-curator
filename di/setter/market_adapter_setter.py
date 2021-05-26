from injector import Module, Binder, singleton

from di import Profile, DISwitcher
from port.adapter.service.market.adapter import MarketAdapter
from port.adapter.service.market.adapter.liquid import LiquidMarketAdapter


class MarketAdapterSetter(Module):
    INTERFACES = {
        Profile({"liquid"}): LiquidMarketAdapter
    }

    def configure(self, binder: Binder) -> None:
        binder.bind(MarketAdapter, to=DISwitcher.get(self.INTERFACES), scope=singleton)
