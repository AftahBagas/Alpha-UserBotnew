from datetime import datetime

from userbot import CMD_HELP, StartTime
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


@ register(outgoing=True, pattern="^.ping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**Ping Userbot 😜**\n"
                    f"➥ **Ping •** "
                    f"`%sms` \n"
                    f"➥ **Uptime •** "
                    f"`{uptime}` \n" % (duration))


@ register(outgoing=True, pattern="^.bping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("**.➠**")
    await pong.edit("**..➠**")
    await pong.edit("**...➠**")
    await pong.edit("**....➠**")
    await pong.edit("**.....➠**")
    await pong.edit("**......➠**")
    await pong.edit("**.......➠**")
    await pong.edit("**PING**")
    await pong.edit("**⚡**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"┍《 **𝘼 𝙇 𝙋 𝙃 𝘼** 》━─\n"
                    f"┟➠  __Ping:__ "
                    f"`%sms` \n"
                    f"┞➠ __Uptime:__ "
                    f"`{uptime}` \n"
                    f"╰━─━───────" % (duration))


CMD_HELP.update(
    {"www": "📚 **Cmd** : `.aping`\
    \n📄 **Descriptions** : Untuk menunjukkan ping bot.\
    \n\n📚 **Cmd** : `.bping`\
    \n📄 **Descriptions** : Untuk menunjukkan ping bot."
     })
