from __future__ import annotations

from enum import Enum


class Currency(Enum):
    """「通貨」

    通貨とは、決済のための価値交換媒体(貨幣)のこと。
    暗号通貨取引や為替取引では、「通貨」=「資産」として捉えることができますが、株式や債券などでは「通貨」=「資産」ではありません。
    (1株式で決済するということができないからです。)そのため、「通貨」と「資産」は別々のドメインオブジェクトとして定義しています。
    """
    # 暗号通貨
    BTC = "BTC"
    ETH = "ETH"
    XRP = "XRP"
    BCH = "BCH"
    SGD = "SGD"
    USDT = "USDT"
    # 法定通貨
    JPY = "JPY"
    USD = "USD"

    @classmethod
    def value_of(cls, name: str) -> Currency:
        for e in cls:
            if e.name == name:
                return e
        raise ValueError("通貨 {} は存在しません。".format(name))
