from datetime import datetime
from typing import Tuple

from injector import inject

from domain.model.asset import Asset
from domain.model.currency import Currency
from domain.model.market.market_service import MarketService
from domain.model.trade import MarketTrades
from port.adapter.service.market.adapter import MarketAdapter


class MarketServiceImpl(MarketService):

    @inject
    def __init__(self, market_adapter: MarketAdapter):
        self.__market_adapter = market_adapter

    def fetch_market_trades(self, pair: Tuple[Asset, Currency], from_datetime: datetime) -> MarketTrades:
        return self.__market_adapter.fetch_market_trades(pair, from_datetime)
