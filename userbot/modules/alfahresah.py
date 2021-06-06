import asyncio
from platform import uname
import time

from userbot import ALIVE_NAME, CMD_HELP, StartTime, bot
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


modules = CMD_HELP


@ register(outgoing=True, pattern=r"^\.(?:salken)\s?(.)?")
async def amireallysalken(salken):
    await bot.get_me()
    await get_readable_time((time.time() - StartTime))
    await salken.edit("Halo Semuanya :)")
    await asyncio.sleep(2)
    await salken.edit("Cuma Mau Bilang")
    await asyncio.sleep(2)
    output = (
        f"`Namaku {DEFAULTUSER} Umur {USER_AGE}`\n"
        f"     `Tunggal Di {COUNTRY} Salam Kenal :)`")

CMD_HELP.update({
    "salken":
    "📚 **Cmd** : `.salken`\
    \n📄 **Descriptions** : Command Salken Untuk Dirimu :)."
})
