# Alfareza
from userbot import bot
from userbot.events import alphabot
from userbot.cmdhelp import CmdHelp


@alphabot(outgoing=True, pattern=r"^\.xogame(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    botusername = "@xobot"
    noob = "play"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, noob)
    await tap[0].click(event.chat_id)
    await event.delete()

# Alfareza


@alphabot(outgoing=True, pattern=r"^\.wp(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    wwwspr = event.pattern_match.group(1)
    botusername = "@whisperBot"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, wwwspr)
    await tap[0].click(event.chat_id)
    await event.delete()

# Alfareza


@alphabot(outgoing=True, pattern=r"^\.mod(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    modr = event.pattern_match.group(1)
    botusername = "@PremiumAppBot"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, modr)
    await tap[0].click(event.chat_id)
    await event.delete()

# Alfareza

CmdHelp('alphafun').add_command(
    '.xogame', None, 'Memainkan Game XO bersama temanmu .'
).add_command(
    'mod', <nama app>, 'Dapatkan Aplikasi mod.'
).add_command(
    'wp', <texs><username/id>, 'Berikan pesan rahasia.'
).add()
