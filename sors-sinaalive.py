"""#Hello. These files are all private to Source Sina. 
#In short, there are files registered for Source, another group. 
#You do not need to write a file from the beginning for the sake of rights, 
#and there are complete files. Thank you for installing Iraq Thun. 
#Our channel is here: https://t.me/telerebo
 . """

import os
import re
import nekos
import requests
import asyncio , time
from PIL import Image
from userbot import StartTime
from telethon import events,version
from platform import python_version, uname
from userbot.utils import admin_cmd,sudo_cmd
from userbot import CMD_HELP, ALIVE_NAME, catdef , catversion

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "cat"
CAT_IMG = Config.ALIVE_PIC

@borg.on(admin_cmd(outgoing=True, pattern="aliv$"))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = alive.message
    uptime = await catdef.get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    hmm = bot.uid
    if alive.reply_to_msg_id:
        reply_to_id = await alive.get_reply_message()
    if CAT_IMG:
        cat_caption  = f"__**🇮🇶 Welcome to sors-sina 📲**__\n\n"
        cat_caption += f"**🃏channel @telerebo Orders @telerebo`\n"   
        cat_caption += f"**🃏THE DAV @telerebo`"
        cat_caption += f"**🃏 Version :** `{catversion}`\n"
        cat_caption += f"**🃏 python :** `{python_version()}\n`"
        cat_caption += f"**🃏 Uptime :** `{uptime}\n`"  
        cat_caption += f"**🃏 My peru Master:** [{DEFAULTUSER}](tg://user?id={hmm})\n"
        await borg.send_file(alive.chat_id, CAT_IMG, caption=cat_caption, reply_to=reply_to_id)
        await alive.delete()
    else:
        await alive.edit(f"__**🇮🇶 Welcome to sors-sina 📲**__\n\n"
                         f"**🃏channel @IRAQTHON Orders @telerebo`\n"   
                         f"**🃏THE DAV @telerebo`"
                         f"**🃏 Version :** `{catversion}`\n"
                         f"**🃏 python :** `{python_version()}\n`"
                         f"**🃏 Uptime :** `{uptime}\n`"  
                         f"**🃏 My Peru Master:** [{DEFAULTUSER}](tg://user?id={hmm})\n"
                        )         

@borg.on(admin_cmd(pattern="cat$"))
async def _(event):
    await event.delete() 
    reply_to_id = event.message
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    with open("temp.png", "wb") as f:
        f.write(requests.get(nekos.cat()).content)
    img = Image.open("temp.png")
    img.save("temp.webp", "webp")
    img.seek(0)
    await bot.send_file(event.chat_id , open("temp.webp", "rb"),reply_to=reply_to_id) 
	
#Hello. These files are all private to Source Sins.
#In short, there are files registered for Source, another group. 
#You do not need to write a file from the beginning for the sake of rights, 
#and there are complete files. Thank you for installing Iraq Thun. 
#Our channel is here: https://t.me/tele_thon


def check_data_base_heal_th():
    # https://stackoverflow.com/a/41961968
    is_database_working = False
    output = "No Database is set"
    if not Var.DB_URI:
        return is_database_working, output
    from userbot.plugins.sql_helper import SESSION
    try:
        # to check database we will execute raw query
        SESSION.execute("SELECT 1")
    except Exception as e:
        output = f"❌ {str(e)}"
        is_database_working = False
    else:
        output = "Functioning Normally"
        is_database_working = True
    return is_database_working, output

CMD_HELP.update({"alive": "`.alive` :\
      \n**USAGE:** status of bot.\
      \n\n`.cat`\
      \n**USAGE : **Random cat stickers"
})
