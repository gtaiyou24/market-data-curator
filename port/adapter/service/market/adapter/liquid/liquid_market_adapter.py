from datetime import datetime
from typing import Tuple

import requests
from requests.models import Response
from retrying import retry

from domain.model.asset import Asset
from domain.model.currency import Currency
from domain.model.trade import MarketTrades
from exception import SystemException, ErrorCode
from others import log
from port.adapter.service.market.adapter import MarketAdapter
from port.adapter.service.market.adapter.liquid.translator import MarketTradesTranslator


class LiquidMarketAdapter(MarketAdapter):
    EXECUTIONS_API = "https://api.liquid.com/executions"

    # see https://api.liquid.com/products
    PRODUCT_ID = {
        ('BTC', 'JPY'): 5,
        ('ETH', 'JPY'): 29,
        ('XRP', 'JPY'): 83,
        ('QASH', 'JPY'): 50,
        ('BCH', 'JPY'): 41
    }

    def __init__(self):
        self.__connection_timeout = 2.0
        self.__read_timeout = 1.0
        self.__market_trades_translator = MarketTradesTranslator()

    @retry(stop_max_attempt_number=3, wait_exponential_multiplier=100)
    def fetch_market_trades(self, pair: Tuple[Asset, Currency], from_datetime: datetime) -> MarketTrades:
        log.info("liquidにリクエストします...")
        try:
            response: Response = requests.get(
                self.EXECUTIONS_API,
                params={
                    "product_id": self.PRODUCT_ID[(pair[0].name, pair[1].value)],
                    "timestamp": int(from_datetime.timestamp()),
                    "limit": 1000
                },
                timeout=(self.__connection_timeout, self.__read_timeout)
            )
            return self.__market_trades_translator.translate(pair, response.json())
        except requests.exceptions.Timeout:
            raise SystemException(ErrorCode.MARKET_2001, "liquidでタイムアウトが発生しました。")
        except Exception as e:
            log.error(e)
            raise SystemException(ErrorCode.MARKET_1001, "liquidで想定外のエラーが発生しました。{}".format(e))
