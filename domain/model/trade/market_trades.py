from dataclasses import dataclass
from typing import Tuple

import pandas as pd

from domain.model.asset import Asset
from domain.model.currency import Currency


@dataclass(init=False, frozen=True, unsafe_hash=True)
class MarketTrades:
    """市場の歩み値(約定)"""
    pair: Tuple[Asset, Currency]
    table: pd.DataFrame

    def __init__(self, pair: Tuple[Asset, Currency], table: pd.DataFrame):
        assert isinstance(table, pd.DataFrame), "約定テーブルにはpandas.DataFrame型を指定してください。"
        assert table.columns.tolist() == ["ID", "Quantity", "Price", "TakerSide", "Timestamp"], \
            "約定テーブルには ['Id','Quantity','Price','TakerSide','Timestamp'] カラムを指定してください"
        assert set(table["TakerSide"].unique()) == {"Buy", "Sell"}, "TakerSideには'Buy','Sell'を指定してください。"
        assert pair, "通貨ペアは必須です。"
        super().__setattr__("pair", pair)
        # 新しい約定が上になるようにする
        super().__setattr__("table", table.sort_values(by="Timestamp", ascending=False))
