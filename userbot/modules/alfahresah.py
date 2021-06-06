import asyncio
import time

from userbot import USER_AGE, ALIVE_NAME, CMD_HELP, StartTime, COUNTRY
from userbot.events import register


# ============== ALPHA USERBOT ===============
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


modules = CMD_HELP


@register(outgoing=True, pattern="^.kickme$")
async def kickme(leave):
    """ Basically it's .kickme command """
    await leave.edit("` {ALIVE_NAME}  Telah Keluar Grup ツ`")
    await leave.client.kick_participant(leave.chat_id, 'me')

CMD_HELP.update({
    "salken":
    "📚 **Cmd** : `.salken`\
    \n📄 **Descriptions** : Command Salken Untuk Dirimu :)."
})
