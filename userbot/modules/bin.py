# Port by Koala @manusiarakitann
# jangan datang hanya saat perlu :) aku bukan tuhan

from telethon import events, functions
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^\.bin ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    danish = event.pattern_match.group(1)
    chat = "@Carol5_bot"
    await event.edit("Sedang Mencari Info BIN..")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1247032902)
            )
            await event.client.send_message(chat, "/bin {}".format(danish))
            respond = await response
        except YouBlockedUserError:
            await event.reply("Unblock dulu @Carol5_bot ")
            return
        if respond.text.startswith(" "):
            await event.edit("That bot is dead bro now this cmd is useless 😂😂")
        else:

            await event.client.send_message(event.chat_id, respond.message)
    await bot(functions.messages.DeleteHistoryRequest(peer=chat, max_id=0))
    await event.delete()


@register(outgoing=True, pattern=r"^\.vbv ?(.*)")
async def _(event):
    if event.fwd_from:
        return

    danish = event.pattern_match.group(1)
    chat = "@Carol5_bot"
    await event.edit("Sedang Mencari Info Card Credit vbv..")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1247032902)
            )
            await event.client.send_message(chat, "/vbv {}".format(danish))
            respond = await response
        except YouBlockedUserError:
            await event.reply("Unblock dulu @Carol5_bot ")
            return
        if respond.text.startswith(" "):
            await event.edit("Bot ny meninggoy asu 😂😂")
        else:

            await event.client.send_message(event.chat_id, respond.message)
    await bot(functions.messages.DeleteHistoryRequest(peer=chat, max_id=0))
    await event.delete()


@register(outgoing=True, pattern=r"^\.iban ?(.*)")
async def _(event):
    if event.fwd_from:
        return

    danish = event.pattern_match.group(1)
    chat = "@Carol5_bot"
    await event.edit("Connecting...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1247032902)
            )
            await event.client.send_message(chat, "/iban {}".format(danish))
            response = await response
        except YouBlockedUserError:
            await event.reply("Boss! Please Unblock @Carol5_bot ")
            return
        if response.text.startswith(" "):
            await event.edit("That bot is dead bro now this cmd is useless 😂😂")
        else:
            await event.client.send_message(event.chat_id, respond.message)
    await bot(functions.messages.DeleteHistoryRequest(peer=chat, max_id=0))
    await event.delete()


CMD_HELP.update(
    {
        "bin": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙 : `bin`\
        \n\n  •  🍁𝘾𝙤𝙢𝙢𝙖𝙣𝙙 : `.bin`\
        \n  •  **Usage : Untuk mencari info bin cc.\
        \n\n  •  🍁𝘾𝙤𝙢𝙢𝙖𝙣𝙙 : `.vbv`\
        \n  •  **Usage : **Checker Card Credit VBV (Verif By Visa).\
        \n\n  •  🍁𝘾𝙤𝙢𝙢𝙖𝙣𝙙 : `.iban`\
        \n  •  **Usage : **Mencari Info Card Iban.\
    "
    }
)
