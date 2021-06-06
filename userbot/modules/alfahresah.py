from time import sleep
from userbot.events import register
from userbot import CMD_HELP, USER_AGE, ALIVE_NAME, COUNTRY


@register(outgoing=True, pattern='^.salken(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Hai Perkenalkan Namaku {ALIVE_NAME}`")
    sleep(3)
    await typew.edit("`Umurku {USER_AGE} Tahun`")
    sleep(1)
    await typew.edit("`Tinggal Di {COUNTRY}, Salam Kenal:)`")


CMD_HELP.update({
    "salken":
    "📚 **Cmd** : `.salken`\
    \n📄 **Descriptions** : Command Salken Untuk Dirimu :)."
})
