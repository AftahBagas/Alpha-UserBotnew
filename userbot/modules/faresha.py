""" Userbot module Memes stikers for deafult user"""

import asyncio

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.ftiker$")
async def ftiker(ftiker):
    """ Basically it's .ftiker command """
    await ftiker.edit(f"https://telegra.ph/file/ac67caadafc18d1dca6f1.png")
    await asyncio.sleep(1)
    await msg.delete()
    await ftiker.edit(f"https://telegra.ph/file/3112b6dd8f4784461f60b.png")
    await asyncio.sleep(1)
    await msg.delete()
    await salken.edit(f"https://telegra.ph/file/f126b88f1eda9935c3c41.png")
    await asyncio.sleep(1)
    await msg.delete()
    await ftiker.edit(f"https://telegra.ph/file/ce0aa3b36fb4aef8ee51f.png")
    await asyncio.sleep(1)
    await msg.delete()
    await salken.edit(f"https://telegra.ph/file/3414ba83f0fa6fac1d670.png")
    await asyncio.sleep(1)
    await msg.delete()
    await salken.edit(f"https://telegra.ph/file/47df342be4d7613066d78.png")


CMD_HELP.update({
    "stikermms":
    "📚 **Cmd** : `.ftiker`\
    \n📄 **Descriptions** : Cek Aja sendiri :v."
})
