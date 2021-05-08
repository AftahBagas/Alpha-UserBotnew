for i in gbanned:
        if i.sender == str(moot.sender_id):
            await moot.delete()


@register(outgoing=True, pattern=r"^\.ungban(?: |$)(.*)")
async def ungbon(un_gban):
    # Admin or creator check
    chat = await un_gban.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    # If not admin and not creator, return
    if not admin and not creator:
        return await un_gban.edit(NO_ADMIN)

    # Check if the function running under SQL mode
    try:
        from userbot.modules.sql_helper.gban_sql import ungban
    except AttributeError:
        return await un_gban.edit(NO_SQL)

    user = await get_user_from_event(un_gban)
    user = user[0]
    if not user:
        return

    # If pass, inform and start ungbanned
    await un_gban.edit("```Menjalankan Global Blokir ! ```")

    if ungban(user.id) is False:
        await un_gban.edit("`Kesalahan! Pengguna Sedang Tidak Di Gban.`")
    else:
        # Inform about success
        await un_gban.edit("```Berhasil! Pengguna Sudah Tidak Lagi Diblokir```")
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
    await gspdr.edit("`Berhasil Memblokir Pengguna!`")
    if gban(user.id) is False:
        await gspdr.edit("`Kesalahan! Pengguna Sudah Diblokir.`")
    else:
        if reason:
            await gspdr.edit(f"**Dibisukan Disemua Media Alpha!**\n**Alasan:** `{reason}`")
        else:
            await gspdr.edit("`Berhasil Memblokir Pengguna Secara Global!`")

        if BOTLOG:
            await gspdr.client.send_message(
                BOTLOG_CHATID,
                "#GLOBALBAN\n"
                f"PENGGUNA: [{user.first_name}](tg://user?id={user.id})\n"
                f"GRUP: {gspdr.chat.title}(`{gspdr.chat_id}`)",
            )
