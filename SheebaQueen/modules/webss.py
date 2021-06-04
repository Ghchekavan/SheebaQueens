from pyrogram import filters

from SheebaQueen.pyrogramee.pluginhelpers import admins_only
from SheebaQueen.services.pyrogram import pbot as app


@app.on_message(filters.command("ss") & ~filters.private & ~filters.edited)
@admins_only
async def take_ss(_, message):
    if len(message.command) != 2:
        await message.reply_text("Give A Url To Fetch Screenshot.")
        return
    url = message.text.split(None, 1)[1]
    m = await message.reply_text("**Taking Screenshot**")
    await m.edit("**Uploading**")
    try:
        await app.send_photo(
            message.chat.id,
            photo=f"https://webshot.amanoteam.com/print?q={url}",
        )
    except TypeError:
        await m.edit("No Such Website.")
        return
    await m.delete()
__mod_name__ = "Web Ss "
__help__ = """
/ss < website url/domain> ===>>  use this module to take like ss of any website
 ×------××----
/ss telegram.org
"""
