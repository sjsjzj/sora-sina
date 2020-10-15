from telethon import events
import random, re
from userbot.utils import admin_cmd
import asyncio 



@borg.on(admin_cmd("zah ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("احبك")
        await asyncio.sleep(4.1)
        await event.edit("دوستت دارم")
        await asyncio.sleep(3.5)
        await event.edit("я люблю тебя")
        await asyncio.sleep(2.2)
        await event.edit("seni seviyorum")
        await asyncio.sleep(3.1)
        await event.edit("사랑해")
        await event.edit("ik hou van je") 
        await asyncio.sleep(3.1)
        
       