#インストールしたdiscord.pyの読み込み
import discord 
import os
#randomモジュールの読み込み
import random
#reライブラリの読み込み
import re
#datetimeの読み込み
import datetime

#翠のトークン
TOKEN = os.environ['DISCORD_BOT_TOKEN']

#接続に必要なオブジェクトを生成
client = discord.Client()
