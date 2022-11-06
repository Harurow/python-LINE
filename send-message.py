#!/usr/local/bin/python3

from linebot.models import TextSendMessage
from linebot import LineBotApi
import os
from dotenv import load_dotenv
load_dotenv(override=True)

# 認証情報は.envから取得する
LINE_CHANNEL_ACCESS_TOKEN = os.getenv('LINE_CHANNEL_ACCESS_TOKEN')
bot = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)

bot.broadcast(TextSendMessage(text="LINE Message APIのブロードキャストによるメッセージ"))
