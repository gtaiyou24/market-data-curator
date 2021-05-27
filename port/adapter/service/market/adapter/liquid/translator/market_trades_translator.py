from typing import Tuple

import pandas as pd

from domain.model.asset import Asset
from domain.model.currency import Currency
from domain.model.trade import MarketTrades


class MarketTradesTranslator:

    def translate(self, pair: Tuple[Asset, Currency], liquid_response_json: dict) -> MarketTrades:
        models = pd.DataFrame(liquid_response_json)
        table = pd.DataFrame(models[["id", "quantity", "price", "taker_side", "timestamp"]])
        table.columns = ["ID", "Quantity", "Price", "TakerSide", "Timestamp"]
        table["TakerSide"].replace({"buy": "Buy", "sell": "Sell"}, inplace=True)
        return MarketTrades(pair, table)
