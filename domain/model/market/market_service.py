import abc
from typing import Tuple

from domain.model.asset import Asset
from domain.model.currency import Currency
from domain.model.trade import MarketTrades


class MarketService(abc.ABC):
    """市場ドメインサービス

    市場データを生成する「ファクトリとしてのドメインサービス」として実装しています。
    """

    @abc.abstractmethod
    def fetch_market_trades(self, pair: Tuple[Asset, Currency]) -> MarketTrades:
        pass
