# coding: utf-8

from flask import Flask, request, abort

# 從linebot 套件包裡引用 LineBotApi 與 WebhookHandler 類別
from linebot import (
    LineBotApi, WebhookHandler
)

# 引用無效簽章錯誤
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import MessageEvent, TextMessage, TextSendMessage

# 載入json處理套件
import json
import configparser
import random



config = configparser.ConfigParser()
config.read('config.ini')
# 載入基礎設定檔

line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
handler = WebhookHandler(config.get('line-bot', 'channel_secret'))

# 設定Server啟用細節
app = Flask(__name__,static_url_path = "/素材" , static_folder = "./素材/")

# 生成實體物件


# 啟動server對外接口，使Line能丟消息進來
@app.route("/", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


# Phoebe愛唱歌
@handler.add(MessageEvent, message=TextMessage)
def pretty_echo(event):
    if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":

        pretty_note = '♫♪♬'
        pretty_text = ''

        for i in event.message.text:
            pretty_text += i
            pretty_text += random.choice(pretty_note)

        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=pretty_text)
        )

import os
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=os.environ['PORT'])

