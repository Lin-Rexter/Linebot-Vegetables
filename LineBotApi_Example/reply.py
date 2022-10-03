# coding=utf-8
from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage)

# 載入LineBot設定檔
from .settings import (line_bot_api, handler, user_id)

# Flask框架初始化
app = Flask(__name__)

@app.route('/')
def hello():
    return f'Hello, World!'

@app.route("/callback", methods=['POST'])
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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

# 回復Line訊息模組
@handler.add(MessageEvent, message=TextMessage)
def line_reply(event=None, spider_name=None):
    user_message = event.message.text
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(
            text=(spider_name(str(user_message)) or user_message)
        )
    )

def line_reply_run():
    if __name__ == "__main__":
        # 執行flask
        app.run()