import asyncio

from SheebaQueen import telethn as sheeba
from telethon import events
import re

@sheeba(events.NewMessage(pattern="(/pprank ?(.*)"))
async def pprank(events):
   
        msg = await eor("**PROMOTING USER..**")
        await asyncio.sleep(1)
        await msg.edit("**PROMOTING USER...**")
        await asyncio.sleep(1)
        await msg.edit("**GIVING RIGHTS**")
        await asyncio.sleep(1)
        await msg.edit("**PROMOTED USER SUCCESSFULLY**")
