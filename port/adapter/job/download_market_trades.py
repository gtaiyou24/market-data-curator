import argparse
from datetime import datetime

from application.command import DownloadMarketTradesCommand
from application.service import MarketTradesApplicationService
from di import DIManager
from others import notice, log

di_manager = DIManager()
download_market_trades_application_service = di_manager.get(MarketTradesApplicationService)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="歩み値をダウンロードします")
    parser.add_argument("asset_name", help="資産名を指定してください。(ex, BTC)", type=str)
    parser.add_argument("currency_name", help="通貨を指定してください。(ex, JPY)", type=str)
    parser.add_argument("start", help="期間開始日を指定してください。(ex, 20210527)", type=str)
    parser.add_argument("end", help="期間終了日を指定してください。(ex, 20210601)", type=str)
    args = parser.parse_args()

    try:
        start = datetime.strptime(args.start, '%Y%m%d')
        end = datetime.strptime(args.end, '%Y%m%d')

        command = DownloadMarketTradesCommand(
            args.asset_name, args.currency_name,
            datetime(start.year, start.month, start.day),
            datetime(end.year, end.month, end.day)
        )

        download_market_trades_application_service.download(command)
    except Exception as e:
        msg = "歩み値ダウンロードジョブの実行中にエラーが発生しました。{}".format(e)
        log.error(msg)
        notice.post(msg)
