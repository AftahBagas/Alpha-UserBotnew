from time import sleep
from userbot.events import register
from userbot import CMD_HELP, USER_AGE, ALIVE_NAME, COUNTRY


@register(outgoing=True, pattern='^.alfareza(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Hai Perkenalkan Namaku Alfareza`")
    sleep(3)
    await typew.edit("`15 Tahun`")
    sleep(1)
    await typew.edit("`Tinggal Di Kota Pati, Salam Kenal:)`")
