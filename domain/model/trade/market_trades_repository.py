import abc
from typing import NoReturn

from domain.model.trade import MarketTrades


class MarketTradesRepository(abc.ABC):

    @abc.abstractmethod
    def save(self, market_trades: MarketTrades) -> NoReturn:
        pass
