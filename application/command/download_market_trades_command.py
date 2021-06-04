from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(init=False, frozen=True, unsafe_hash=True)
class DownloadMarketTradesCommand:
    asset_name: str
    currency_name: str
    period: Period

    def __init__(self, asset_name: str, currency_name: str, start: datetime, end: datetime):
        assert asset_name, "資産を指定してください。(ex. BTC)"
        assert currency_name, "通貨を指定してください。(ex. JPY)"
        super().__setattr__("asset_name", asset_name)
        super().__setattr__("currency_name", currency_name)
        super().__setattr__("period", DownloadMarketTradesCommand.Period(start, end))

    @dataclass(init=False, frozen=True, unsafe_hash=True)
    class Period:
        start: datetime
        end: datetime

        def __init__(self, start: datetime, end: datetime):
            assert start, "期間開始日を指定してください。"
            assert end, "期間終了日を指定してください。"
            assert end > start, "開始日、終了日の関係が不正です。終了日 > 開始日の関係にしてください。"
            super().__setattr__("start", start)
            super().__setattr__("end", end)
