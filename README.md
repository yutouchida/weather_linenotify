# 天気をLINEに通知するPythonスクリプト

Pythonの仮想環境を作成できることが前提です。また、Macでのみ動作確認済みです。

## 環境構築
`python3 -m venv env && source env/bin/activate && pip install -r requirements.txt`

## .envファイル作成
`echo 'LINE_NOTIFY_TOKEN=（LINEのアクセストークンを指定）
ADDRESS=（天気を取得したい都道府県・市を指定）' > .env`

## 実行
`python weather.py`
