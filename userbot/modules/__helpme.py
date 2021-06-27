
from userbot import BOT_USERNAME
from userbot.events import alphabot


@alphabot(outgoing=True, pattern="^.helpme")
async def yardim(event):
    bangreza = BOT_USERNAME
    if bangreza is not None:
        results = await event.client.inline_query(
            bangreza,
            f"{BOT_USERNAME}"
        )
        await results[0].click(
            event.chat_id,
            reply_to=event.reply_to_msg_id,
            hide_via=True
        )
        await event.delete()
    else:
        await event.edit(["NO_BOT"])
