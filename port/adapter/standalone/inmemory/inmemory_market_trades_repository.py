import atexit
from typing import NoReturn, Dict, Tuple

import pandas as pd

from domain.model.asset import Asset
from domain.model.currency import Currency
from domain.model.trade import MarketTradesRepository, MarketTrades


class InMemoryMarketTradesRepository(MarketTradesRepository):

    def __init__(self):
        self.__market_trades_dict: Dict[Tuple[Asset, Currency]: MarketTrades] = {}

        # プログラム終了時に保存する
        atexit.register(self.__to_csv)

    def save(self, market_trades: MarketTrades) -> NoReturn:
        if market_trades.pair not in self.__market_trades_dict.keys():
            self.__market_trades_dict[market_trades.pair] = market_trades
        else:
            concat_table = pd.concat([
                market_trades.table, self.__market_trades_dict[market_trades.pair].table
            ]).drop_duplicates(keep='first')
            self.__market_trades_dict[market_trades.pair] = MarketTrades(market_trades.pair, concat_table)

    def __to_csv(self):
        for pair, market_trades in self.__market_trades_dict.items():
            market_trades.table.to_csv(
                "{}{}-market-trades.csv.gz".format(pair[0].name, pair[1].name),
                compression='gzip'
            )
