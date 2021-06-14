from telethon.tl.types import ChannelParticipantAdmin as admin
from telethon.tl.types import ChannelParticipantCreator as owner
from telethon.tl.types import UserStatusOffline as off
from telethon.tl.types import UserStatusOnline as onn
from telethon.tl.types import UserStatusRecently as rec
from telethon.utils import get_display_name

from userbot.events import register
from userbot import CMD_HELP


@register(
    outgoing=True,
    pattern=r"^\.tag(on|off|all|bots|rec|adm|own)?(.*)",
    disable_errors=True,
)
async def _(e):
    okk = e.text
    lll = e.pattern_match.group(2)
    users = 0
    o = 0
    nn = 0
    rece = 0
    if lll:
        xx = f"{lll}"
    else:
        xx = ""
    async for bb in e.client.iter_participants(e.chat_id, 99):
        users = users + 1
        x = bb.status
        y = bb.participant
        if isinstance(x, onn):
            o = o + 1
            if "on" in okk:
                xx += f"\n[{get_display_name(bb)}](tg://user?id={bb.id})"
        if isinstance(x, off):
            nn = nn + 1
            if "off" in okk:
                if not (bb.bot or bb.deleted):
                    xx += f"\n[{get_display_name(bb)}](tg://user?id={bb.id})"
        if isinstance(x, rec):
            rece = rece + 1
            if "rec" in okk:
                if not (bb.bot or bb.deleted):
                    xx += f"\n[{get_display_name(bb)}](tg://user?id={bb.id})"
        if isinstance(y, owner):
            if "admin" or "owner" in okk:
                xx += f"\n👑 [{get_display_name(bb)}](tg://user?id={bb.id}) 👑"
        if isinstance(y, admin):
            if "admin" in okk:
                if not bb.deleted:
                    xx += f"\n[{get_display_name(bb)}](tg://user?id={bb.id})"
        if "all" in okk:
            if not (bb.bot or bb.deleted):
                xx += f"\n[{get_display_name(bb)}](tg://user?id={bb.id})"
        if "bot" in okk:
            if bb.bot:
                xx += f"\n[{get_display_name(bb)}](tg://user?id={bb.id})"
    await e.client.send_message(e.chat_id, xx)
    await e.delete()


CMD_HELP.update({
    'tag':
    "📚 **Cmd** : `.tag all`"
    "\n📄 **Descriptions** : Tag 100 member di Grup."
    "\n\n📚 **Cmd** : `.tag admin`"
    "\n📄 **Descriptions** : Tag Admins di grup."
    "\n\n📚 **Cmd** : `.tag own`"
    "\n📄 **Descriptions** : Tag Owner Di grup"
    "\n\n📚 **Cmd** : `.tag bot`"
    "\n📄 **Descriptions** : Tag Bots Di Grup."
    "\n\n📚 **Cmd** : `.tag rec`"
    "\n📄 **Descriptions** : Tag member baru off di grup."
    "\n\n📚 **Cmd** : `.tag on`"
    "\n📄 **Descriptions** : Tag online Members(work only if privacy off)."
    "\n\n📚 **Cmd** : `.tag off`"
    "\n📄 **Descriptions** : Tag Offline Members(work only if privacy off)."
})
