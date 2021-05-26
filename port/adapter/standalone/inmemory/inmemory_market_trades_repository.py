from typing import NoReturn, Dict, Tuple

import pandas as pd

from domain.model.asset import Asset
from domain.model.currency import Currency
from domain.model.trade import MarketTradesRepository, MarketTrades


class InMemoryMarketTradesRepository(MarketTradesRepository):

    def __init__(self):
        self.__market_trades_dict: Dict[Tuple[Asset, Currency]: MarketTrades] = {}

    def save(self, market_trades: MarketTrades) -> NoReturn:
        if not market_trades.pair in self.__market_trades_dict.keys():
            self.__market_trades_dict[market_trades.pair] = market_trades
        else:
            concat_table = pd.concat([market_trades.table, self.__market_trades_dict[market_trades.pair].table])
            self.__market_trades_dict[market_trades.pair] = MarketTrades(market_trades.pair, concat_table)
