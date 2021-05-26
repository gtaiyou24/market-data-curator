import argparse

from application.service import DownloadMarketTradesApplicationService
from di import DIManager
from others import notice


di_manager = DIManager()
download_market_trades_application_service = di_manager.get(DownloadMarketTradesApplicationService)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="歩み値をダウンロードします")
    parser.add_argument("asset_name", help="資産名を指定してください。(ex, BTC)", type=str)
    parser.add_argument("currency_name", help="通貨を指定してください。(ex, JPY)", type=str)
    args = parser.parse_args()

    try:
        download_market_trades_application_service.download(args.asset_name, args.currency_name)
    except Exception as e:
        notice.post("歩み値ダウンロードジョブの実行中にエラーが発生しました。{}".format(e))
