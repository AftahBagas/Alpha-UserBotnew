from userbot.events import register
from userbot import CMD_HELP


@register(outgoing=True, pattern=r"^\.hii$")
async def sayhi(e):
    await e.edit(
        "\n✨✨✨✨✨✨✨✨✨✨✨✨"
        "\n✨🌹🌹✨✨🌹🌹✨✨🌹🌹✨"
        "\n✨🌹🌹✨✨🌹🌹✨✨🌹🌹✨"
        "\n✨🌹🌹✨✨🌹🌹✨✨🌹🌹✨"
        "\n✨🌹🌹🌹🌹🌹🌹✨✨🌹🌹✨"
        "\n✨🌹🌹🌹🌹🌹🌹✨✨🌹🌹✨"
        "\n✨🌹🌹✨✨🌹🌹✨✨🌹🌹✨"
        "\n✨🌹🌹✨✨🌹🌹✨✨🌹🌹✨"
        "\n✨🌹🌹✨✨🌹🌹✨✨🌹🌹✨"
        "\n✨✨✨✨✨✨✨✨✨✨✨✨")


CMD_HELP.update({
    "hii":
    "📚 **Cmd** : `.hii`\
    \n📄 **Descriptions** : pesan untuk hiiiiiiii."
})
