# Mau Maling Kah?
# Silahkan Maling Aja Xixixi
# Gak Usah Sungkan

from time import sleep
from userbot import CMD_HELP
from userbot.events import register

# Enjoy


@register(outgoing=True, pattern='^.masok(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**masok**")
    sleep(1)
    await typew.edit("pak")
    sleep(1)
    await typew.edit("eko")
    sleep(1)
    await typew.edit("masuk pak eko")


@register(outgoing=True, pattern='^.tele(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("PC")
    sleep(1)
    await typew.edit("lanjut vc")
    sleep(1)
    await typew.edit("nyaman")
    sleep(1)
    await typew.edit("dighosting")
    await typew.edit("siklus player tele")


@register(outgoing=True, pattern='^.bacot(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("nyenyenyenye")
    sleep(1)
    await typew.edit("apasih ngomong apa")
    sleep(1)
    await typew.edit("gajelas anjir")


@register(outgoing=True, pattern='^.linkk(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("1")
    sleep(1)
    await typew.edit("2")
    sleep(1)
    await typew.edit("3")
    sleep(1)
    await typew.edit("4")
    sleep(1)
    await typew.edit("5")
    sleep(1)
    await typew.edit("6")
    sleep(1)
    await typew.edit("7")
    sleep(1)
    await typew.edit("8")
    sleep(1)
    await typew.edit("9")
    sleep(1)
    await typew.edit("10")
    sleep(1)
    await typew.edit("[jangan dipencet anjir](https://pornhub.com)")


@register(outgoing=True, pattern='^.pesawat(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`mo naik pesawat`")
    sleep(1)
    await typew.edit("`🛫`")
    await typew.edit("`Landing dulu`")
    await typew.edit("`🛫`")
    await typew.edit("`sjhzajjs`")
    await typew.edit("`🛬`")
    await typew.edit("`eh oleng`")
    await typew.edit("`dan gak jadi terbang🙂`")


@register(outgoing=True, pattern='^.emot(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`😀`")
    await typew.edit("`😃`")
    await typew.edit("`😄`")
    await typew.edit("`😁`")
    await typew.edit("`😆`")
    await typew.edit("`😅`")
    await typew.edit("`😂`")
    await typew.edit("`🤣`")
    await typew.edit("`😭`")
    await typew.edit("`😗`")
    await typew.edit("`😙`")
    await typew.edit("`😚`")
    await typew.edit("`😘`")
    await typew.edit("`🥰`")
    await typew.edit("`😍`")
    await typew.edit("`🤩`")
    await typew.edit("`🥳`")
    await typew.edit("`🤗`")
    await typew.edit("`🙃`")
    await typew.edit("`🙂`")
    await typew.edit("`Dahlah Capek`")
    await typew.edit("`Cek sendiri di keyboardmu`")
    await typew.edit("`🥵`")


@register(outgoing=True, pattern='^.alfabot(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Userbot ?`")
    sleep(1)
    await typew.edit("`⚡`")
    sleep(1)
    await typew.edit("`I am Alpha Userbot`")


@register(outgoing=True, pattern='^.kabar(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**`Assalamualaikum`**")
    sleep(2)
    await typew.edit("**`Apa Kabar Semuanya`**")


@register(outgoing=True, pattern='^.repoalpha(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("⚡")
    sleep(2)
    await typew.edit("**😈Alpha Userbot😈**\n\n [Tekan sini](https://github.com/AftahBagas/Alpha-Userbot)")

# Ini Tercipta Hasil Gabut Doang

CMD_HELP.update({
    "animasi4":
    "📚 **Cmd** : .masok\
    \n📄 **Descriptions** : cek aja males jelasin\
    \n\n📚 **Cmd** : .tele\
    \n📄 **Descriptions** : siklus player tele\
    \n\n📚 **Cmd** : .bacot\
    \n📄 **Descriptions** : cek aja\
    \n\n📚 **Cmd** : .alfabot\
    \n📄 **Descriptions** : cek aja sendiri\
    \n\n📚 **Cmd** : .pesawat\
    \n📄 **Descriptions** : pesawat oleng\
    \n\n📚 **Cmd** : .emot\
    \n📄 **Descriptions** : jenis jenis emot\
    \n\n📚 **Cmd** : .kabar\
    \n📄 **Descriptions** : Cek Aja dh sndri\
    \n\n📚 **Cmd** : .linkk\
    \n📄 **Descriptions** : kshsjwkhsgshsj."


})
