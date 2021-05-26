from typing import Tuple

import requests

from domain.model.asset import Asset
from domain.model.currency import Currency
from domain.model.trade import MarketTrades
from port.adapter.service.market.adapter import MarketAdapter
from port.adapter.service.market.adapter.liquid.translator import MarketTradesTranslator


class LiquidMarketAdapter(MarketAdapter):
    LIQUID_PRODUCT_IDS = {
        ('BTC', 'JPY'): 5
    }

    def __init__(self):
        self.market_trades_translator = MarketTradesTranslator()

    def fetch_market_trades(self, pair: Tuple[Asset, Currency]) -> MarketTrades:
        params = {
            "product_id": self.LIQUID_PRODUCT_IDS[(pair[0].name, pair[1].name)],
            "limit": 1000
        }
        response: requests.models.Response = requests.get("https://api.liquid.com/executions", params=params)
        return self.market_trades_translator.translate(pair, response.json())
