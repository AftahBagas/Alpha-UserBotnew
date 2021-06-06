""" Userbot module salken for deafult user"""

import asyncio

from userbot import ALIVE_NAME, CMD_HELP, COUNTRY, USER_AGE
from userbot.events import register


@register(outgoing=True, pattern="^.salken$")
async def salken(salken):
    """ Basically it's .salken command """
    await salken.edit(f"`Halo Namaku {ALIVE_NAME}`")
    await asyncio.sleep(2)
    await salken.edit(f"`Umurku {USER_AGE}`")
    await asyncio.sleep(2)
    await salken.edit(f"`Tinggal Di {COUNTRY} Salam Kenal :)`")


CMD_HELP.update({
    "salken":
    "📚 **Cmd** : `.salken`\
    \n📄 **Descriptions** : Command Salken Untuk Dirimu :)."
})
