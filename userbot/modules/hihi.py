from userbot.events import register
from userbot import CMD_HELP


@register(outgoing=True, pattern=r"^\.hihi$")
async def sayhi(e):
    await e.edit(
        "\n🌺✨✨🌺✨🌺🌺🌺"
        "\n🌺✨✨🌺✨✨🌺✨"
        "\n🌺🌺🌺🌺✨✨🌺✨"
        "\n🌺✨✨🌺✨✨🌺✨"
        "\n🌺✨✨🌺✨🌺🌺🌺"
        "\n☁️☁️☁️☁️☁️☁️☁️☁️")


CMD_HELP.update({
    "hihi":
    "📚 **Cmd** : `.hihi`\
    \n📄 **Descriptions** : pesan untuk hiiiiiiii."
})
