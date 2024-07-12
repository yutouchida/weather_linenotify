import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

# .envファイルのパスを指定して読み込む
load_dotenv(dotenv_path='.env')

#LINE Notifyと連携するためのtoken
line_notify_token = os.getenv('LINE_NOTIFY_TOKEN')
line_notify_api = 'https://notify-api.line.me/api/notify'

# 取得したい都道府県・市を指定
address = os.getenv('ADDRESS')

# 緯度経度を取得
geocoding_Url = "https://www.geocoding.jp/api/"
geocoding_Params = {"q":address}
geocoding_Req = requests.get(geocoding_Url, params=geocoding_Params)
geocoding_Soup = BeautifulSoup(geocoding_Req.content, "xml") 
Lat = geocoding_Soup.find("lat").text
Lng =  geocoding_Soup.find("lng").text

# WeatherNewsの取得
WeatherNewsUrl = "https://weathernews.jp/onebox/"

# 緯度経度を取得
SrhUrl = WeatherNewsUrl + Lat + '/' + Lng + "/lang=ja"

weathernews_Req = requests.get(SrhUrl)
weathernews_Soup = BeautifulSoup(weathernews_Req.text, "html.parser")

wc = weathernews_Soup.find(class_="nowWeather")

#.strip():前後の空白文字の削除・.splitlines():改行コードで分割
ws = [i.strip() for i in wc.text.splitlines()]

#リスト内包表記で""でないものをリスト化
wl = [i for i in ws if i != ""]

message = (
    f"\n{address}の天気\n\n天気:{wl[0]}\n{wl[2]}:{wl[6]}\n{wl[3]}:{wl[7]}\n{wl[4]}:{wl[8]}\n{wl[5]}:{wl[9]}\n提供元:{SrhUrl}"
)

#LINENotifyへ通知の記述
payload = {'message': message}
headers = {'Authorization': 'Bearer ' + line_notify_token} 
line_notify = requests.post(line_notify_api, data=payload, headers=headers)

print(f"以下の通知がLINEに送信されました。\n----------{message}\n----------")
