""" Userbot module salken for deafult user"""

from asyncio import sleep
from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP, bot, ALIVE_NAME, USER_AGE, COUNTRY
from datetime import datetime
from telethon import functions
from emoji import emojize
from math import sqrt
from telethon.tl.functions.channels import GetFullChannelRequest, GetParticipantsRequest
from telethon.tl.functions.messages import GetFullChatRequest, GetHistoryRequest
from telethon.tl.types import MessageActionChannelMigrateFrom, ChannelParticipantsAdmins
from telethon.errors import (
    ChannelInvalidError,
    ChannelPrivateError,
    ChannelPublicGroupNaError)
from telethon.utils import get_input_location
from telethon.tl.types import ChannelParticipantAdmin, ChannelParticipantsBots
from userbot.events import register
from userbot.modules.admin import get_user_from_event
from telethon.utils import pack_bot_file_id




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
