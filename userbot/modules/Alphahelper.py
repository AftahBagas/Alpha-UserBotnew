""" Userbot module for other small commands. """
from userbot import ALIVE_NAME
from userbot.events import alphabot

from userbot.cmdhelp import CmdHelp


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@alphabot(outgoing=True, pattern="^.lhelp$")
async def usit(e):
    await e.edit(
        f"**Hai Pengguna {DEFAULTUSER} Kalau Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        "\n[Telegram](t.me/Kanjengingsun)"
        "\n[Repo](https://github.com/Aftahbagas/Alpha-Userbot)"
        "\n[Instagram](Instagram.com/Aftahbagas)")


@alphabot(outgoing=True, pattern="^.vars$")
async def var(m):
    await m.edit(
        f"**Disini Daftar Vars Dari {DEFAULTUSER}:**\n"
        "\n[DAFTAR VARS](https://raw.githubusercontent.com/Aftahbagas/Alpha-Userbot/Alpha/varshelper.txt)")


CmdHelp('alphahelper').add_command(
    'lhelp', None, 'Bantuan Untuk Alpha Userbot.'
).add_command(
    'vars', None, 'untuk melihat beberapa daftar vars.'
).add()
