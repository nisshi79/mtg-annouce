# coding: utf-8
import discord
from discord.ext import tasks
import datetime
import toml
import os

TOKEN = os.environ['DISCORD_BOT_TOKEN']

mtgs = toml.load(open('./mtgs.toml'))

print(mtgs)

client = discord.Client()

@client.event
async def on_ready():
    #起動時に呼ばれるメソッド
    print('-----Logged in info-----')
    print(client.user.name)
    print(client.user.id)
    print('------------------------')


@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    now = datetime.datetime.now().strftime('%a %H:%M')
    tomorrowDate = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%Y'+r'%2F'+'%m'+r'%2F'+'%d')
    for mtg in mtgs.values():
        if now == mtg['annouceTiming']:
            await client.wait_until_ready()
            channel = client.get_channel(mtg['channelId'])
            print(channel)
            announceMessage = mtg['message'].format(mtgDate=tomorrowDate)
            await channel.send(announceMessage)

#ループ処理実行
loop.start()
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)