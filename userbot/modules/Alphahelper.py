""" Userbot module for other small commands. """
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.lhelp$")
async def usit(e):
    await e.edit(
        f"**Hai Pengguna {DEFAULTUSER} Kalau Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        "\n[Telegram](t.me/Kanjengingsun)"
        "\n[Repo](https://github.com/Aftahbagas/Alpha-Userbot)"
        "\n[Instagram](Instagram.com/Aftahbagas)")


@register(outgoing=True, pattern="^.vars$")
async def var(m):
    await m.edit(
        f"**Disini Daftar Vars Dari {DEFAULTUSER}:**\n"
        "\n[DAFTAR VARS](https://raw.githubusercontent.com/Aftahbagas/Alpha-Userbot/Alpha/varshelper.txt)")


CMD_HELP.update({
    "Alphahelper":
    "`.lhelp`\
\nPenjelasan: Bantuan Untuk Alpha.\
\n`.vars`\
\nPenjelasan: Untuk Melihat Beberapa Daftar Vars."
})
