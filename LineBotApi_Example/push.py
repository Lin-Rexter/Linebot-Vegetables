# coding=utf-8
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage)

# 載入LineBot設定檔
from .settings import (line_bot_api, handler, user_id)

#推送Line訊息模組
def line_push(messages):
    line_bot_api.push_message(
        user_id,
        TextSendMessage(
            text=messages
        )
    )