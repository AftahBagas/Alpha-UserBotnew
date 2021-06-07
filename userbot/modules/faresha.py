""" Userbot module Memes tmoji"""

import asyncio

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.tmoji$")
async def tmoji(tmoji):
    """ Basically it's .tmoji command """
    await tmoji.edit(f"😆")
    await asyncio.sleep(2)
    await tmoji.edit(f"😁")
    await asyncio.sleep(2)
    await tmoji.edit(f"🤣")
    await asyncio.sleep(2)
    await tmoji.edit(f"😂")


CMD_HELP.update({
    "tmoji":
    "📚 **Cmd** : `.tmoji`\
    \n📄 **Descriptions** : Cek Aja sendiri :v."
})
