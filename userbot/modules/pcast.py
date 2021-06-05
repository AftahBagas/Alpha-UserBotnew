# yang nyolong mati
# by Alfareza @kanjengingsun
# alpha userbot


from userbot.events import register
from userbot import CMD_HELP, bot


@register(outgoing=True, pattern=r"^\.pcast(?: |$)(.*)")
async def gucast(event):
    xx = event.pattern_match.group(1)
    if not xx:
        return await event.edit("`Berikan beberapa teks untuk Siaran Global Personal`")
    tt = event.text
    msg = tt[7:]
    kk = await event.edit("`Sedang Mengirim pesan persoalan secara global...`")
    er = 0
    done = 0
    async for x in bot.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            try:
                done += 1
                await bot.send_message(chat, msg)
            except BaseException:
                er += 1
    await kk.edit(f"Berhasil Mengirim Pesan Ke `{done}` obrolan, kesalahan dalam `{er}` obrolan(s)")


CMD_HELP.update(
    {
        "pcast": "📚 **Cmd** : `.pcast`\
         \n📄 **Descriptions** : Mengirim Pesan persoalan Secara Global"
    }
)
