from time import sleep
from userbot.cmdhelp import CmdHelp
from userbot.events import alphabot


@alphabot(outgoing=True, pattern='^.sadboi(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Pertama-tama aku suka kamu`")
    sleep(2)
    await typew.edit("`Kedua ternyata kamu udah ada yg punya:(`")
    sleep(1)
    await typew.edit("`Dan yang terakhir adalah aku sakit hati`")
# Create by myself @localheart


@alphabot(outgoing=True, pattern='^.hai1(?: |$)(.*)')
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


@alphabot(outgoing=True, pattern='^.gabung(?: |$)(.*)')
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

CmdHelp('alpha2').add_command(
    'hai1', None, 'Animasi hallo.'
).add_command(
    'gabung', None, 'Animasi mau gabung.'
).add_command(
    'sadboi', None, 'Curhatan Hati Sadboy Kedua.'
).add()
