# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module containing commands related to the \
    Information Superhighway (yes, Internet). """

from datetime import datetime

from speedtest import Speedtest
from userbot import CMD_HELP, StartTime, ALIVE_NAME
from userbot.events import register
import time


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["Dtk", "Mnt", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(
            seconds, 60) if count < 3 else divmod(
            seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@register(outgoing=True, pattern="^.sping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("**□□□□□ 0%**")
    await pong.edit("**■□□□□ 20%**")
    await pong.edit("**■■□□□ 40%**")
    await pong.edit("**■■■□□ 60%**")
    await pong.edit("**■■■■□ 80%**")
    await pong.edit("**■■■■■ 100%**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"╭ **Ping Userbot!!** \n"
                    f"├🏓 **Pong** • `%sms` \n"
                    f"├🤵 **Pengguna** • `{ALIVE_NAME}` \n"
                    f"╰─────────────" % (duration))


@ register(outgoing=True, pattern="^.lping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("**✎﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏**")
    await pong.edit("**✎﹏﹏﹏﹏﹏﹏﹏**")
    await pong.edit("**✎﹏﹏﹏﹏﹏**")
    await pong.edit("**✎﹏﹏﹏**")
    await pong.edit("**✎﹏**")
    await pong.edit("**✎**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**Pong!!**\n"
                    f"✘ **Ping:** "
                    f"`%sms` \n"
                    f"✘ **Uptime:** "
                    f"`{uptime}` \n" % (duration))


@ register(outgoing=True, pattern="^.xping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**< Pong!! 😈 >**\n"
                    f"➨ **Ping • ** "
                    f"`%sms` \n"
                    f"➨ **Uptime • ** "
                    f"`{uptime}` \n" % (duration))


@ register(outgoing=True, pattern="^.aping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("`Pong!`")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"╭ **Pong Userbot !!**\n"
                    f"├🏓 Ping "
                    f"• `%sms` \n"
                    f"├⏱️ Uptime "
                    f"• `{uptime}` \n"
                    f"╰──────────── " % (duration))


@ register(outgoing=True, pattern="^.sinyal$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("`Mengecek Sinyal...`")
    await pong.edit("**0% ▒▒▒▒▒▒▒▒▒▒**")
    await pong.edit("**20% ██▒▒▒▒▒▒▒▒**")
    await pong.edit("**40% ████▒▒▒▒▒▒**")
    await pong.edit("**60% ██████▒▒▒▒**")
    await pong.edit("**80% ████████▒▒**")
    await pong.edit("**100% ██████████**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"《 𝙎𝙞𝙣𝙮𝙖𝙡 𝘼𝙡𝙥𝙝𝙖 》\n"
                    f"**➥ Sinyal  :** "
                    f"`%sms` \n"
                    f"**➥ Online  :** "
                    f"`{uptime}` \n"
                    f"**➥ Owner  :** `{ALIVE_NAME}`" % (duration))


@ register(outgoing=True, pattern="^.speed$")
async def speedtst(spd):
    """ For .speed command, use SpeedTest to check server speeds. """
    await spd.edit("`Menjalankan Tes Kecepatan Tinggi...🚀`")
    test = Speedtest()

    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()

    await spd.edit("**Hasil Tes:\n**"
                   "🌀 **Dimulai Pada:** "
                   f"`{result['timestamp']}` \n"
                   f" **━━━━━━━━━━━━━━━━━**\n\n"
                   "🌀 **Download:** "
                   f"`{speed_convert(result['download'])}` \n"
                   "🌀 **Upload:** "
                   f"`{speed_convert(result['upload'])}` \n"
                   "🌀 **Ping:** "
                   f"`{result['ping']}` \n"
                   "🌀 **ISP:** "
                   f"`{result['client']['isp']}` \n"
                   "🌀 **BOT:** `Alpha`")


def speed_convert(size):
    """
    Hi human, you can't read bytes?
    """
    power = 2**10
    zero = 0
    units = {0: '', 1: 'Kb/s', 2: 'Mb/s', 3: 'Gb/s', 4: 'Tb/s'}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"


@ register(outgoing=True, pattern="^.pong$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    start = datetime.now()
    await pong.edit("`Pong.....🔨`")
    end = datetime.now()
    duration = (end - start).microseconds / 9000
    await pong.edit("✧ **Pong!**\n`%sms`" % (duration))

CMD_HELP.update(
    {"ping": "📚 **Cmd** : `.ping` ; `.lping` ; `.xping` ; `.sping`\
    \n📄 **Descriptions** : Untuk menunjukkan ping bot.\
    \n\n📚 **Cmd** : `.speed`\
    \n📄 **Descriptions** : Untuk menunjukkan kecepatan.\
    \n\n📚 **Cmd** : `.pong`\
    \n📄 **Descriptions** : sama kaya perintah ping."
     })
CMD_HELP.update(
    {"sinyal": "📚 **Plugins** : `Sinyal`\
    \n\n📚 **Cmd** : `.sinyal`\
    \n📄 **Descriptions** : __Untuk melihat sinyal bot__"})
