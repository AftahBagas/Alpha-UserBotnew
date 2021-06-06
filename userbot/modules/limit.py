from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import CMD_HELP, bot
from userbot.events import register


@register(outgoing=True, pattern=r'^.limit(?: |$")
async def demn(ult):
    chat = "@SpamBot"
    msg = await event.edit("Checking If You Are Limited...")
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1743866353)
            )
            await conv.send_message("/start")
            response = await response
            await bot.send_read_acknowledge(chat)
        except YouBlockedUserError:
            await steal.reply("Alpha User! Please Unblock @SpamBot ")
            return
        await msg.edit(f"~ {response.message.message}")


CMD_HELP.update({
    "limited":
    "📚 **Cmd** : `.limit`\
\n📄 **Descriptions** : Mengecek limit
})