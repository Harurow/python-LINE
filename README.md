# Pythonつかって LINE でメッセージ送信

## 用途

タイトル通りpythonを利用してLINEでメッセージを送信します

## 準備

* pythonが利用できる環境
* `line-bot-sdk`が利用できる環境
* `python-dotenv`が利用できる環境
* LINE API認証情報

### `line-bot-sdk`,`python-dotenv`について

`line-bot-sdk`,`python-dotenv`を利用しているので事前に`pip`または`pip3`でインストールが必要です

```sh
# 例
pip install line-bot-sdk python-dotenv
```

### LINE API認証情報について

LINEを外部から利用する場合、認証情報が別途必要です。
必要に応じて別途発行してください。必要な情報は、

* LINE_CHANNEL_ACCESS_TOKEN

となります。

セキュリティの関係上、今回のコードには記載しておらず
`.env`ファイルに以下のような形で記載しています。

```sh:.env
LINE_CHANNEL_ACCESS_TOKEN="xxxxx....
```

また`.gitignore`で`.env`を追加しているので`git`の追跡対象外にしています。

### 注意事項

今回のメッセージはブロードキャスト送信です。BOTを友達に追加しているユーザに一斉にメッセージを送信します。
