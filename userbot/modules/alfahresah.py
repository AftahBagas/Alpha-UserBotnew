""" Userbot module salken for deafult user"""

import asyncio

from userbot import ALIVE_NAME, CMD_HELP, COUNTRY, USER_AGE
from userbot.events import alphabot

from userbot.cmdhelp import CmdHelp


@alphabot(outgoing=True, pattern="^.salken$")
async def salken(salken):
    """ Basically it's .salken command """
    await salken.edit(f"`Halo Namaku {ALIVE_NAME}`")
    await asyncio.sleep(2)
    await salken.edit(f"`Umurku {USER_AGE}`")
    await asyncio.sleep(2)
    await salken.edit(f"`Tinggal Di {COUNTRY} Salam Kenal :)`")


CmdHelp('animasi2').add_command(
    'salken', None, 'Kata Kata Untuk Salken Dirimu.'
).add()
