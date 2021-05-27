from typing import NoReturn

from injector import inject

from domain.model.asset import Asset
from domain.model.currency import Currency
from domain.model.market.market_service import MarketService
from domain.model.trade import MarketTrades, MarketTradesRepository
from exception import SystemException


class DownloadMarketTradesApplicationService:
    """取引所の歩み値をダウンロードするアプリケーションサービス"""

    @inject
    def __init__(self,
                 market_service: MarketService,
                 market_trades_repository: MarketTradesRepository):
        self.__market_service = market_service
        self.__market_trades_repository = market_trades_repository

    def download(self, asset_name: str, currency_name: str) -> NoReturn:
        asset = Asset(asset_name)
        currency = Currency(currency_name)

        try:
            market_trades: MarketTrades = self.__market_service.fetch_market_trades((asset, currency))
            self.__market_trades_repository.save(market_trades)
        except SystemException as e:
            e.logging()
