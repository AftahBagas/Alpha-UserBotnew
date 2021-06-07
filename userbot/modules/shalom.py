""" Userbot module for other small commands. """

from random import randint
from asyncio import sleep
from os import execl
import sys
import os
import io
import sys
import json
from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP, bot
from userbot.events import register

@register(outgoing=True, pattern="^.shalom$")
async def shalom(e):
    await e.edit(
        "\n☁️☁️☁️☁️☁️☁️☁️☁️☁️"
        "\n☁️⭐️☁️☁️☁️⭐️⭐️☁️☁️"
        "\n☁️⭐️☁️☁️⭐️☁️☁️⭐️☁️"
        "\n☁️⭐️☁️☁️⭐️☁️☁️⭐️☁️"
        "\n☁️⭐️☁️☁️⭐️☁️☁️⭐️☁️"
        "\n☁️☁️⭐️⭐️☁️☁️☁️⭐️☁️"
        "\n☁️☁️☁️☁️☁️☁️☁️☁️☁️"
        "\n☁️⭐️⭐️⭐️⭐️⭐️⭐️⭐️☁️"
        "\n☁️☁️☁️☁️⭐️☁️☁️☁️☁️"
        "\n☁️☁️☁️☁️⭐️☁️☁️☁️☁️"
        "\n☁️☁️☁️☁️⭐️☁️☁️☁️☁️"
        "\n☁️⭐️⭐️⭐️⭐️⭐️⭐️⭐️☁️"
        "\n☁️☁️☁️☁️☁️☁️☁️☁️☁️"
        "\n☁️⭐️⭐️⭐️⭐️⭐️⭐️☁️☁️"
        "\n☁️☁️☁️☁️⭐️☁️☁️⭐️☁️"
        "\n☁️☁️☁️☁️⭐️☁️☁️⭐️☁️"
        "\n☁️☁️☁️☁️⭐️☁️☁️⭐️☁️"
        "\n☁️⭐️⭐️⭐️⭐️⭐️⭐️☁️☁️"
        "\n☁️☁️☁️☁️☁️☁️☁️☁️☁️"
        "\n☁️⭐️⭐️⭐️⭐️⭐️⭐️⭐️☁️"
        "\n☁️⭐️☁️☁️☁️☁️☁️☁️☁️"
        "\n☁️⭐️☁️☁️☁️☁️☁️☁️☁️"
        "\n☁️⭐️☁️☁️☁️☁️☁️☁️☁️"
        "\n☁️⭐️☁️☁️☁️☁️☁️☁️☁️"
        "\n☁️☁️☁️☁️☁️☁️☁️☁️☁️"
        "\n☁️☁️⭐️⭐️⭐️⭐️⭐️☁️☁️"
        "\n☁️⭐️☁️☁️☁️☁️☁️⭐️☁️"
        "\n☁️⭐️☁️☁️☁️☁️☁️⭐️☁️"
        "\n☁️⭐️☁️☁️☁️☁️☁️⭐️☁️"
        "\n☁️☁️⭐️⭐️⭐️⭐️⭐️☁️☁️"
        "\n☁️☁️☁️☁️☁️☁️☁️☁️☁️"
        "\n☁️⭐️⭐️⭐️⭐️⭐️⭐️⭐️☁️"
        "\n☁️☁️☁️☁️☁️☁️⭐️☁️☁️"
        "\n☁️☁️☁️☁️⭐️⭐️☁️☁️☁️"
        "\n☁️☁️☁️☁️☁️☁️⭐️☁️☁️"
        "\n☁️⭐️⭐️⭐️⭐️⭐️⭐️⭐️☁️"
        "\n☁️☁️☁️☁️☁️☁️☁️☁️☁️")
    
    CMD_HELP.update({
    'shalom':
    '📚 **Cmd** : `.shalom`\
\n📄 **Descriptions** : memberikan SHALOM yang bagus sebagai output.'
})
