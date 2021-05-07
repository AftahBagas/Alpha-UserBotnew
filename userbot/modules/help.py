# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Alpha help command """


import asyncio
from userbot import CMD_HELP
from userbot.events import register

modules = CMD_HELP


@register(outgoing=True, pattern="^.help(?: |$)(.*)")
async def help(lord):
    """ For .help command,"""
    args = alpha.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await alpha.edit(str(CMD_HELP[args]))
        else:
            await alpha.edit("**Maaf Alpha, Saya Tidak Punya Perintah Itu ツ**")
            await asyncio.sleep(200)
            await alpha.delete()
    else:
        await alpha.edit("🍁")
        await alpha.edit("**🍁 Mᴏᴅᴜʟᴇs 1:**\n"
                         "`admin`  `adzan`  `afk`  `gabut`  `vip`  `animasi`  `android`  `anime`  `anti_spambot`  `aria`  `ascii`\n\n"
                         "**🍁 Mᴏᴅᴜʟᴇs 2:**\n"
                         "`blacklist`  `carbon`   `chat`  `mutechat`  `covid`  `membuat`  `deepfry`  `emojigames`\n\n"
                         "**🍁 Mᴏᴅᴜʟᴇs 3:**\n"
                         "`eval`  `exec`  `term`  `fakegban`  `federations`  `figlet`  `filter`  `gban`  `gcast`  `gdrive`  `gcommit`  `github`\n\n"
                         "**🍁 Mᴏᴅᴜʟᴇs 4:**\n"
                         "`glitch`  `gps`  `hash`  `base64`  `hentai`  `heroku`  `id`  `imgmeme`  `kekuatan`\n\n"
                         "**🍁 Mᴏᴅᴜʟᴇs 5:**\n"
                         "`lastfm`  `locks`  `lord`  `aeshtetic`  `deteksi`  `alphafun`  `alphahelper`  `hazmat`\n\n"
                         "**🍁 Mᴏᴅᴜʟᴇs 6:**\n"
                         "`instagram`  `amongus`  `alphamemes`  `misc`  `app`  `undelete`  `grab`  `clone`\n\n"
                         "**🍁 Mᴏᴅᴜʟᴇs 7:**\n"
                         "`randomprofil`  `song`  `tiny`  `tempmail`  `tiktok`  `wordcloud`\n\n"
                         "**🍁 Mᴏᴅᴜʟᴇs 8:**\n"
                         "`lyrics`  `mega`  `memes`  `memify`  `mentions`  `purge`  `purgeme`  `del`  `edit`\n\n"
                         "**🍁 Mᴏᴅᴜʟᴇs 9:**\n"
                         "`sd`  `random`  `sleep`  `shutdown`  `repo`  `readme`  `repeat`  `restart`\n\n"
                         "**🍁 Mᴏᴅᴜʟᴇs 10:**\n"
                         "`raw`  `nekobot`  `notes`  `off`  `phreaker`  `pm`  `profil`  `quotly`  `rastick`  `resi`  `reverse`  `salam`  `sangmata`\n\n"
                         "**🍁 Mᴏᴅᴜʟᴇs 11:**\n"
                         "`santetonline`  `image_search`  `currency`  `google`  `wiki`  `ud`  `tts`  `translate`  `youtube`  `rip`\n\n"
                         "**🍁 Mᴏᴅᴜʟᴇs 12:**\n"
                         "`removebg`  `ocr`  `qrcode`  `barcode`  `paste`  `getpaste`  `nekobin`  `direct`  `screenshot`  `sed`  `snips`  `spam`  `spotifynow`  `ssvideo`\n\n"
                         "**🍁 Mᴏᴅᴜʟᴇs 13:**\n"
                         "`stickers`  `stickers2`  `sysd`  `botver`  `pip`  `alive`  `tag_all`  `telegraph`  `timedate`  `torrent`\n\n"
                         "**🍁 Mᴏᴅᴜʟᴇs 14:**\n"
                         "`transform`  `update`  `download`  `getid`  `waifu`  `wallpaper`  `weather`\n\n"
                         "**🍁 Mᴏᴅᴜʟᴇs 15:**\n"
                         "`webupload`  `welcome`  `whois`  `ping`  `sinyal`  `xiaomi`  `zipfile`")
        await alpha.reply("\n**Cara Menggunakan,** **Contoh:**\n**Ketik** `.help afk` **Untuk Iinformasi Modules**\n**GROUP SUPPORT:** [TEKAN](t.me/petercord)")
        await asyncio.sleep(1000)
        await alpha.delete()
