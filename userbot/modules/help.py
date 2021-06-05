# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot help command """

import asyncio
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register
from platform import uname

modules = CMD_HELP

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.help(?: |$)(.*)")
async def help(event):
    """ For .help command,"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit("**`User Alpha, Command Yang Anda Cari Tidak Ditemukan 😔`**")
            await asyncio.sleep(200)
            await event.delete()
    else:
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += "`\t |  "
        await event.edit("**⚙️ Alpha Userbot ⚙️**\n\n"
                         f"**🤵 Pengguna : {DEFAULTUSER}**\n**📚 Modules : {len(modules)}**\n\n"
                         "**➦ Main Menu :**\n"
                         f"| {string}\n\n")
        await event.reply(f"\n**Contoh** : Ketik <`.help afk`> Untuk Informasi Pengunaan.\nAtau Bisa Juga Ketik `.helpme` Untuk Main Menu Yang Lain-Nya.")
        await asyncio.sleep(1000)
        await event.delete()
