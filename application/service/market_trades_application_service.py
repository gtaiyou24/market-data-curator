from datetime import datetime
from typing import NoReturn

from injector import inject

from application.command import DownloadMarketTradesCommand
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

    def download(self, command: DownloadMarketTradesCommand) -> NoReturn:
        asset = Asset(command.asset_name)
        currency = Currency(command.currency_name)
        pair = (asset, currency)

        log.info("{}/{}の歩み値をダウンロードします".format(asset.name, currency.name))

        # ダウンロードする期間を指定
        _from = command.period.start
        _to = command.period.end
        while True:
            try:
                # 取引所から歩み値を取得します
                market_trades: MarketTrades = self.__market_service.fetch_market_trades(pair, _from)

                # 取得した歩み値を保存します
                self.__market_trades_repository.save(market_trades)

                # 最後の約定日時のタイムスタンプを取得する
                last_timestamp = market_trades.last_timestamp()
                log.info("最終約定日時: {}".format(datetime.fromtimestamp(int(last_timestamp))))

                # 指定した日時まで取得できたら処理を止める
                if last_timestamp > _to.timestamp():
                    break

                if last_timestamp != _from.timestamp():
                    _from = datetime.fromtimestamp(int(last_timestamp))
                else:
                    # 最初の約定日時と最後の約定日時が同じ場合、同じ_from値でリクエストしてしまうので+1する
                    _from = datetime.fromtimestamp(int(last_timestamp + 1))
            except SystemException as e:
                e.logging()
                break

        log.info("{}/{}の歩み値をダウンロードが完了しました".format(asset.name, currency.name))
