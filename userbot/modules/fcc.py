
from faker import Faker

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^\.fcc(?: |$)(.*)")
async def fcc(alfarezavent):
    if geezevent.fwd_from:
        return
    alfarezacc = Faker()
    alfarezaname = alfarezacc.name()
    alfarezaadre = alfarezacc.address()
    alfarezacard = alfarezacc.credit_card_full()

    await edit_or_reply(alfarezaevent, f"__**🤵 Nama :- **__\n`{alfarezaname}`\n\n__**🏡 ADDRESS :- **__\n`{alfarezaadre}`\n\n__**💳 CARD :- **__\n`{alfarezacard}`")


CMD_HELP.update({
    "fcc":
    "📚 **Cmd** : `.fcc`\
    \n📄 **Descriptions** : mendapatkan informasi fake cc."
})
