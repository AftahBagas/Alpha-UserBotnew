# alfareza

from time import sleep
from userbot.cmdhelp import CmdHelp
from userbot.events import alphabot


@alphabot(outgoing=True, pattern="^.pe$")
async def koc(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("p")
        await e.edit("pe")
        await e.edit("woi p")
        await e.edit("p")
        await e.edit("pe")
        await e.edit("p")
        await e.edit("pppp")
        await e.edit("p")
        await e.edit("pe")
        await e.edit("p")
        await e.edit("pe")
        await e.edit("sori kwand ini otomatis")
        await e.edit("pe")
        await e.edit("p")
        await e.edit("pe")
        await e.edit("masih bot ni")
        await e.edit("pe")
        await e.edit("p")
        await e.edit("pe")
        await e.edit("ppppp")
        await e.edit("panjang benerπ")
        await e.edit("π")
        await e.edit("p mulu")
        await e.edit("maklum gabut")
        await e.edit("gaada kerjaan")
        await e.edit("dahlah")
        await e.edit("(males lah")
        await e.edit("udah ni udah")
        await e.edit("π")
        await e.edit("p")


@alphabot(outgoing=True, pattern='^.hoh(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n(\\_/)`"
                     "`\n(β_β)`"
                     "`\n />β€οΈ *Ini Buat Kamu`")
    sleep(3)
    await typew.edit("`\n(\\_/)`"
                     "`\n(β_β)`"
                     "`\n/>π  *eh patah`")
    sleep(2)
    await typew.edit("`\n(\\_/)`"
                     "`\n(β_β)`"
                     "`\nπ<\\  *aku ambil lagi deh`")


@alphabot(outgoing=True, pattern='^.noh(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n(\\_/)`"
                     "`\n(ββΏβ)`"
                     "`\n />πΉ *Ini Buat Kamu`")
    sleep(2)
    await typew.edit("`\n(\\_/)`"
                     "`\n(β‘βΏβ‘)`"
                     "`\nπ₯<\\  *Gajadi Layu`")

# alfareza


CmdHelp('animasi4').add_command(
    'pe', None, 'Animasi Gaje wkw.'
).add_command(
    'hoh', None, 'Animasi Kasih Hati Tapi Gajadi.'
).add_command(
    'noh', None, 'Animasi Kasih Bunga Tapi Gajadi.'
).add()
