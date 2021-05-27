from datetime import datetime
from typing import NoReturn

from injector import inject

from domain.model.asset import Asset
from domain.model.currency import Currency
from domain.model.market.market_service import MarketService
from domain.model.trade import MarketTrades, MarketTradesRepository
from exception import SystemException
from others import log


class MarketTradesApplicationService:
    """取引所の歩み値をダウンロードするアプリケーションサービス"""

    @inject
    def __init__(self,
                 market_service: MarketService,
                 market_trades_repository: MarketTradesRepository):
        self.__market_service = market_service
        self.__market_trades_repository = market_trades_repository

    def download(self, asset_name: str, currency_name: str, from_datetime: datetime, to_datetime: datetime) -> NoReturn:
        log.info("{}/{}の歩み値をダウンロードします".format(asset_name, currency_name))

        asset = Asset(asset_name)
        currency = Currency(currency_name)
        pair = (asset, currency)

        _from = from_datetime
        while True:
            try:
                log.info("取引所から歩み値を取得します")
                market_trades: MarketTrades = self.__market_service.fetch_market_trades(pair, _from)

                log.info("取得した歩み値を保存します")
                self.__market_trades_repository.save(market_trades)

                # 最後の約定日時のタイムスタンプを取得する
                last_timestamp = market_trades.last_timestamp()
                if last_timestamp > to_datetime.timestamp():
                    # 指定した日時まで取得できたら処理を止める
                    break

                if last_timestamp == _from.timestamp():
                    _from = datetime.fromtimestamp(int(last_timestamp + 1))
                else:
                    _from = datetime.fromtimestamp(int(last_timestamp))
            except SystemException as e:
                e.logging()
                break

        log.info("{}/{}の歩み値をダウンロードが完了しました".format(asset_name, currency_name))
