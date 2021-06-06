from userbot import CMD_HELP, bot
from userbot.events import register


@register(outgoing=True, pattern=r"^\.xogame(?: |$)(.*)")
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


@register(outgoing=True, pattern=r"^\.whisp(?: |$)(.*)")
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


@register(outgoing=True, pattern=r"^\.mod(?: |$)(.*)")
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


@register(outgoing=True, pattern=r"^\.game(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    modr = event.pattern_match.group(1)
    botusername = "@gamee"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, modr)
    await tap[0].click(event.chat_id)
    await event.delete()

CMD_HELP.update({
    "games": "\
📚 **Cmd** : `.xogame`\
\n📄 **Descriptions** : Mainkan game XO bersama temanmu.\
\n\n📚 **Cmd** : `.mod <nama app>`\
\n📄 **Descriptions** : Dapatkan applikasi mod\
\n\n📚 **Cmd** : `.game <nama game>`\
\n📄 **Descriptions** : Dapatkan Game Untuk di mainkan\
\n\n📚 **Cmd** : `.whisp <teks> <username>`\
\n📄 **Descriptions** : Berikan pesan rahasia"})
