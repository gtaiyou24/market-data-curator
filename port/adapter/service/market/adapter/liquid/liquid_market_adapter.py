from typing import Tuple

import requests
from requests.models import Response
from retrying import retry

from domain.model.asset import Asset
from domain.model.currency import Currency
from domain.model.trade import MarketTrades
from exception import SystemException, ErrorCode
from port.adapter.service.market.adapter import MarketAdapter
from port.adapter.service.market.adapter.liquid.translator import MarketTradesTranslator


class LiquidMarketAdapter(MarketAdapter):
    EXECUTIONS_API = "https://api.liquid.com/executions"

    PRODUCT_ID = {
        ('BTC', 'JPY'): 5
    }

    def __init__(self):
        self.__market_trades_translator = MarketTradesTranslator()

    @retry(stop_max_attempt_number=3, wait_exponential_multiplier=100)
    def fetch_market_trades(self, pair: Tuple[Asset, Currency]) -> MarketTrades:
        try:
            response: Response = requests.get(
                self.EXECUTIONS_API,
                params={"product_id": self.PRODUCT_ID[(pair[0].name, pair[1].name)], "limit": 1000}
            )

            if response.status_code == 404:
                raise SystemException(ErrorCode.MARKET_1002,
                                      "liquidで404エラーが発生しました。url is {}".format(self.EXECUTIONS_API))

            return self.__market_trades_translator.translate(pair, response.json())

        except requests.exceptions.ConnectTimeout:
            raise SystemException(ErrorCode.MARKET_2001, "liquidでタイムアウトが発生しました。")

        except Exception as e:
            raise SystemException(ErrorCode.MARKET_1001, "liquidで想定外のエラーが発生しました。{}".format(e))
