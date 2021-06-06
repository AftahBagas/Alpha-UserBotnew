import asyncio
from time import sleep
from userbot.events import register
from userbot import CMD_HELP ALIVE_NAME USER_AGE COUNTRY


@ register(outgoing=True, pattern=r"^\.(?:salken)\s?(.)?")
async def amireallysalken(salken):
    user = await bot.get_me()
    await get_readable_time((time.time() - StartTime))
    await salken.edit("Halo Namaku {ALIVE_NAME}")
    await asyncio.sleep(2)
    await salken.edit("Umurku {USER_AGE} Tahun")
    await asyncio.sleep(2)
    await salken.edit("Tinggal Di {COUNTRY} Salam Kenal :)")


CMD_HELP.update({
    "salken":
    "📚 **Cmd** : `.salken`\
    \n📄 **Descriptions** : Command Salken Untuk Dirimu :)."
})
