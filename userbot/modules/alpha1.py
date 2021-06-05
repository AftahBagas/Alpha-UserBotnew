from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.sadboy2(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Pertama-tama aku suka kamu`")
    sleep(2)
    await typew.edit("`Kedua ternyata kamu udah ada yg punya:(`")
    sleep(1)
    await typew.edit("`Dan yang terakhir adalah aku sakit hati`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.hai1(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n┻┳|―-∩`"
                     "`\n┳┻|     ヽ`"
                     "`\n┻┳|    ● |`"
                     "`\n┳┻|▼) _ノ`"
                     "`\n┻┳|￣  )`"
                     "`\n┳ﾐ(￣ ／`"
                     "`\n┻┳T￣|`"
                     "\n**Hallo**")


@register(outgoing=True, pattern='^.gabung(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n┻┳|―-∩`"
                     "`\n┳┻|     ヽ`"
                     "`\n┻┳|    ● |`"
                     "`\n┳┻|▼) _ノ`"
                     "`\n┻┳|￣  )`"
                     "`\n┳ﾐ(￣ ／`"
                     "`\n┻┳T￣|`"
                     "\n**Boleh Gabung Gak?**")


# Create by myself @localheart

CMD_HELP.update({
    "alpha1":
    "📚 **Cmd** : `.alpha`\
    \n📄 **Descriptions** : alive bot.\
    \n\n📚 **Cmd** : `.sadboy2`\
    \n📄 **Descriptions** : hiks\
    \n\n📚 **Cmd** : `.hai1` ; `.gabung`\
    \n📄 **Descriptions** : coba aja."
})
