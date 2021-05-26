# market-data-curator
市場データを収集するシステム

```bash
# dockerイメージのbuild
$ cd /path/to/market-data-curator
$ docker build -t market-data-curator:latest .
$ docker image ls | grep market-data-curator
```

## ジョブ一覧

### 歩み値のダウンロード
```bash
$ cp .env.sample .env
$ docker container run --rm \
    -v `pwd`:/market-data-curator/ \
    --env-file=.env \
    market-data-curator:latest \
    python port/job/download_market_trades.py BTC JPY
```
