import argparse
from datetime import datetime

from application.service import MarketTradesApplicationService
from di import DIManager
from others import notice


di_manager = DIManager()
download_market_trades_application_service = di_manager.get(MarketTradesApplicationService)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="歩み値をダウンロードします")
    parser.add_argument("asset_name", help="資産名を指定してください。(ex, BTC)", type=str)
    parser.add_argument("currency_name", help="通貨を指定してください。(ex, JPY)", type=str)
    parser.add_argument("_from", help="期間開始日を指定してください。(ex, 20210527)", type=str)
    parser.add_argument("_to", help="期間終了日を指定してください。(ex, 20210601)", type=str)
    args = parser.parse_args()

    try:
        from_datetime = datetime.strptime(args._from, '%Y%m%d')
        to_datetime = datetime.strptime(args._to, '%Y%m%d')

        download_market_trades_application_service.download(
            args.asset_name, args.currency_name,
            datetime(from_datetime.year, from_datetime.month, from_datetime.day),
            datetime(to_datetime.year, to_datetime.month, to_datetime.day)
        )
    except Exception as e:
        notice.post("歩み値ダウンロードジョブの実行中にエラーが発生しました。{}".format(e))
