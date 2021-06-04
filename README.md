# Market Data Curator
市場データを収集するシステム

```bash
# market-data-curatorリポジトリに移動
$ cd /path/to/market-data-curator
# dockerイメージのbuild
$ docker build -t market-data-curator:latest .
# ビルドされていることを確認
$ docker image ls | grep market-data-curator
```

## ジョブ一覧

### 歩み値の一括ダウンロード
```bash
# 環境変数ファイルをコピー
$ cp .env.sample .env

# 適切な値に書き換える
$ vi .env

# 実行する(この例では、2021年04月17日から2021年04月18日までのBTC/JPYの歩み値をダウンロードします)
$ docker container run --rm \
    -v `pwd`:/market-data-curator/ \
    --env-file=.env \
    market-data-curator:latest \
    python port/adapter/job/download_market_trades.py BTC JPY 20210417 20210418
```
