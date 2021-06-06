from userbot.events import register


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
    "gabut":
    "📚 **Cmd** : `.hii`\
    \n📄 **Descriptions** : pesan untuk hiiiiiiii."
})
