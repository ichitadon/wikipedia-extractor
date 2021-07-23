# wikipedia-extractor
## 準備するデータ
WikipediaのCirrusSearch用のdumpデータを[こちら](https://dumps.wikimedia.org/other/cirrussearch/)から事前にダウンロードする。

- 記事データ
  - jawiki-{yyyymmdd}-cirrussearch-content.json.gz
- 記事以外のデータ
  - jawiki-{yyyymmdd}-cirrussearch-gneral.json.gz

CirrusSearchの詳細は、MediaWikiの[Help](https://www.mediawiki.org/wiki/Help:CirrusSearch/ja)を参照。

## 実行環境
### docker build
```
docker build -t wikipedia-extractor .
```

### docker run
```
docker run -v $PWD:/app -it wikipedia-extractor bash
```
## 処理実行
### 記事のメタデータを抽出する
以下のメタデータを抽出する。

- タイトル
- カテゴリのリスト
- リダイレクトのタイトルリスト

dockerの実行環境にデータ（`jawiki-{yyyymmdd}-cirrussearch-content.json.gz`）をマウントしてbashで入り、以下を実行。

```
poetry run python wikipedia_extractor/extract/content.py {入力データのファイルパス} {出力データのファイルパス}
```

### カテゴリのメタデータを抽出する
以下のメタデータを抽出する。

- タイトル
- カテゴリのリスト
- リダイレクトのタイトルリスト

dockerの実行環境にデータ（`jawiki-{yyyymmdd}-cirrussearch-general.json.gz`）をマウントしてbashで入り、以下を実行。

```
poetry run python wikipedia_extractor/extract/general.py {入力データのファイルパス} {出力データのファイルパス}
```

## テスト実行
## run lint
```
docker run -v $PWD:/app -it wikipedia-extractor ./run_lint.sh
```

## run test
```
docker run -v $PWD:/app -it wikipedia-extractor ./run_test.sh
```
