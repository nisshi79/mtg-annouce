# coding: utf-8
import discord
from discord.ext import tasks
import datetime
import pprint

TOKEN = os.environ['DISCORD_BOT_TOKEN']
CHANNEL_ID = os.environ['CHANNEL_ID']

client = discord.Client()

@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    now = datetime.datetime.now()
    currentDoW = now.strftime('%a')
    currentTime = now.strftime('%H:%M')
    tomorrowDate = (now + datetime.timedelta(days=1)).strftime('%Y'+'%2F'+'%m'+'%2F'+'%d')
    # For Mon MTG
    if currentDoW == 'Mon' and currentTime == '17:00':
        await client.wait_until_ready()
        channel = client.get_channel(CHANNEL_ID)
        print(channel)
        announceMassage = '''   
            <@&723890274635612161>
            月曜18:00-MTGのアジェンダです！
            ※５分前集合、揃い次第STARTで早く始め、早く終わりましょう！

            進捗・扱いたいことはscrapboxに18:00までに書き込んでおいてください！

            https://scrapbox.io/per-lxp-bonding/{mtgDate}%E6%9C%88%E6%9B%9CMTG

            Zoom:
            西村 惟 is inviting you to a scheduled Zoom meeting.

            Topic: 月曜MTG
            Time: This is a recurring meeting Meet anytime

            Join Zoom Meeting
            https://zoom.us/j/94878540644?pwd=UkpaejIxSTNjaUV3M2grTWh6dGhoUT09

            Meeting ID: 948 7854 0644
            Passcode: 409818
            One tap mobile
            +16699006833,,94878540644#,,,,,,0#,,409818# US (San Jose)
            +19292056099,,94878540644#,,,,,,0#,,409818# US (New York)

            Dial by your location
                    +1 669 900 6833 US (San Jose)
                    +1 929 205 6099 US (New York)
                    +1 253 215 8782 US (Tacoma)
                    +1 301 715 8592 US (Germantown)
                    +1 312 626 6799 US (Chicago)
                    +1 346 248 7799 US (Houston)
            Meeting ID: 948 7854 0644
            Passcode: 409818
            Find your local number: https://zoom.us/u/abyVEzNlz5
        '''.format(mtgDate=tomorrowDate)
        await channel.send(announceMassage)  

    # For Wed MTG
    elif currentDoW == 'Tue' and currentTime== '17:00':
        await client.wait_until_ready()
        channel = client.get_channel(CHANNEL_ID)
        announceMassage = '''   
            <@&723890274635612161>
            水曜18:30-MTGのアジェンダです！
            ※５分前集合、揃い次第STARTで早く始め、早く終わりましょう！

            進捗・扱いたいことはscrapboxに明日18:30までに書き込んでおいてください！

            https://scrapbox.io/per-lxp-bonding/{mtgDate}%E6%B0%B4%E6%9B%9C%E5%AE%9A%E4%BE%8BMTG

            西村 惟 is inviting you to a scheduled Zoom meeting.

            Topic: PER_LXP_水曜MTG
            Time: This is a recurring meeting Meet anytime

            Join Zoom Meeting
            https://zoom.us/j/92826571853?pwd=aVNVYm43UWNFbWFqQ0ViUGpITG1PQT09

            Meeting ID: 928 2657 1853
            Passcode: 519074
            One tap mobile
            +13017158592,,92826571853#,,,,,,0#,,519074# US (Germantown)
            +13126266799,,92826571853#,,,,,,0#,,519074# US (Chicago)

            Dial by your location
                    +1 301 715 8592 US (Germantown)
                    +1 312 626 6799 US (Chicago)
                    +1 346 248 7799 US (Houston)
                    +1 669 900 6833 US (San Jose)
                    +1 929 205 6099 US (New York)
                    +1 253 215 8782 US (Tacoma)
            Meeting ID: 928 2657 1853
            Passcode: 519074
            Find your local number: https://zoom.us/u/abaNSkGivn
        '''.format(mtgDate=tomorrowDate)
        await channel.send(announceMassage)

#ループ処理実行
loop.start()
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)