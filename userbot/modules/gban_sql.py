@register(incoming=True)
async def muter(moot):
    try:
        from userbot.modules.sql_helper.gban_sql import is_gbanned
        from userbot.modules.sql_helper.spam_ban_sql import is_banned
    except AttributeError:
        return
    banned = is_banned(moot.chat_id)
    gbanned = is_gbanned(moot.sender_id)
    rights = ChatBannedRights(
        until_date=None,
        send_messages=True,
        send_media=True,
        send_stickers=True,
        send_gifs=True,
        send_games=True,
        send_inline=True,
        embed_links=True,
    )
    if banned:
        for i in banned:
            if str(i.sender) == str(moot.sender_id):
                await moot.delete()
                await moot.client(
                    EditBannedRequest(moot.chat_id, moot.sender_id, rights)
                )
    for i in gbanned:
        if i.sender == str(moot.sender_id):
            await moot.delete()


@register(outgoing=True, pattern=r"^\.ungban(?: |$)(.*)")
async def ungmoot(un_gban):
    # Admin or creator check
    chat = await un_gban.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    # If not admin and not creator, return
    if not admin and not creator:
        return await un_gban.edit(NO_ADMIN)

    # Check if the function running under SQL mode
    try:
        from userbot.modules.sql_helper.gban_sql import ungmute
    except AttributeError:
        return await un_gmute.edit(NO_SQL)

    user = await get_user_from_event(un_gban)
    user = user[0]
    if not user:
        return

    # If pass, inform and start ungmuting
    await un_gban.edit("```Menjalankan Global Banned ! ```")

    if ungban(user.id) is False:
        await un_gban.edit("`Kesalahan! Pengguna Sedang Tidak Di Gban.`")
    else:
        # Inform about success
        await un_gban.edit("```Berhasil! Pengguna Sudah Tidak Lagi Dibanned```")
        await sleep(3)
        await un_gban.delete()

        if BOTLOG:
            await un_gban.client.send_message(
                BOTLOG_CHATID,
                "#UNGBAN\n"
                f"PENGGUNA: [{user.first_name}](tg://user?id={user.id})\n"
                f"GRUP: {un_gban.chat.title}(`{un_gban.chat_id}`)",
            )


@register(outgoing=True, pattern=r"^\.gban(?: |$)(.*)")
async def gspider(gspdr):
    # Admin or creator check
    chat = await gspdr.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    # If not admin and not creator, return
    if not admin and not creator:
        return await gspdr.edit(NO_ADMIN)

    # Check if the function running under SQL mode
    try:
        from userbot.modules.sql_helper.gban_sql import gban
    except AttributeError:
        return await gspdr.edit(NO_SQL)

    user, reason = await get_user_from_event(gspdr)
    if not user:
        return

    # If pass, inform and start gbaning
    await gspdr.edit("`Berhasil Membanned Pengguna!`")
    if gban(user.id) is False:
        await gspdr.edit("`Kesalahan! Pengguna Sudah Dibanned.`")
    else:
        if reason:
            await gspdr.edit(f"**Dibanned Disemua Media Lord Java!**\n**Alasan:** `{reason}`")
        else:
            await gspdr.edit("`Berhasil Banned Pengguna Secara Global!`")

        if BOTLOG:
            await gspdr.client.send_message(
                BOTLOG_CHATID,
                "#GLOBALBAN\n"
                f"PENGGUNA: [{user.first_name}](tg://user?id={user.id})\n"
                f"GRUP: {gspdr.chat.title}(`{gspdr.chat_id}`)",
            )
