import os
from telethon import TelegramClient, events
from telethon.sessions import StringSession
import asyncio
import random
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "adubot is alive"

def run():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()

api_id = 32135350
api_hash = "7c9832d6ef116e3d75ac843dbc1bbbad"
session = "1BVtsOIQBu0e_nOgzSD9kxe8NDmuteul2liYvgPlPu3HMJl9ux0Izlg5lceEu631PyIZogd9BI13IwEXGbZ9kyMm82cl7C-2zogtj9fx1ZMIHnjXK02nobKVhYJGQWK429ThrzMqgENCOOfMyrTsGimHE6Siuhxw0RikyoN69sX3QshcIXjdVcHKnaeQRgNqjoT40KzVwa1IhJEQUbmfciu7zWN4eLHT6jQY3xwDW9-XveqagucxBEJyYialU5o5MbXREKBRgzRYrYleC9uYl1jmpq_rpsIUi6gH4ftHrpXa_muicmqXtTt0BXWyoL2yth_F0UQm6yXTIT3w2vYGfJDDr-Uv9qmQ="

client = TelegramClient(StringSession(session), api_id, api_hash)

@client.on(events.NewMessage(incoming=True))
async def auto_reply(event):
    if event.is_private and not event.out:
        if event.raw_text.lower() in ["hi", "hello"]:
            async with client.action(event.chat_id, 'typing'):
                await asyncio.sleep(random.randint(2,4))
            await event.reply('''🐣🦋 𝗡𝗔𝗩𝗬𝗔 𝗔𝗩𝗔𝗜𝗟𝗔𝗕𝗟𝗘 🐣🦋

       🍒  𝗩𝗢𝗜𝗖𝗘 𝗖𝗔𝗟𝗟  🍒

🍒𝟱 𝗠𝗜𝗡𝗨𝗧𝗘𝗦 - 𝟮𝟬𝟬 𝗥𝗦 💦
🍒𝟭𝟬 𝗠𝗜𝗡𝗨𝗧𝗘𝗦 - 𝟯𝟱𝟬 𝗥𝗦 💦

       🎀 𝗩𝗜𝗗𝗘𝗢 𝗖𝗔𝗟𝗟 💘

🍒𝟱 𝗠𝗜𝗡𝗨𝗧𝗘𝗦 - 𝟱𝟬𝟬 𝗥𝗦  💦
🍒𝟭𝟬 𝗠𝗜𝗡𝗨𝗧𝗘𝗦 - 𝟴𝟬𝟬 𝗥𝗦 💦

       🌟 𝗦𝗘𝗫 𝗖𝗛𝗔𝗧 👄

🍒𝟱 𝗠𝗜𝗡𝗨𝗧𝗘𝗦 - 𝟮𝟬𝟬 𝗥𝗦 💦
🍒𝟭𝟬 𝗠𝗜𝗡𝗨𝗧𝗘𝗦 - 𝟯𝟱𝟬 𝗥𝗦 💦

       🎀 𝗦𝗣𝗘𝗖𝗜𝗔𝗟 𝗦𝗛𝗢𝗪 💘

🍒 𝗦𝗔𝗥𝗘𝗘 𝗦𝗛𝗢𝗪 - 𝟭𝟮𝟬𝟬 𝗥𝗦 💦
🍒 𝗦𝗤𝗨𝗜𝗥𝗧 𝗦𝗛𝗢𝗪 - 𝟭𝟭𝟬𝟬 𝗥𝗦 💦

💟𝗗𝗘𝗠𝗢 - 𝟭𝟬𝟬 𝗥𝗦💟''')

@client.on(events.NewMessage(incoming=True))
async def auto_delete_group_messages(event):
    if event.is_group:
        await asyncio.sleep(120)
        try:
            await event.delete()
        except Exception as e:
            print(f"Delete failed: {e}")

@client.on(events.ChatAction())
async def auto_delete_service(event):
    if event.is_group:
        await asyncio.sleep(120)
        try:
            await event.delete()
        except Exception as e:
            print(f"Service delete failed: {e}")

@client.on(events.NewMessage(outgoing=True, pattern=r"\.boost"))
async def boost_msg(event):
    await event.edit("Boost this to get a free kiss. \nt.me/wifeswapping_live?boost ❤️")

@client.on(events.NewMessage(outgoing=True, pattern=r"\.alive"))
async def alive_msg(event):
    await event.edit("I'm alive my queen.. ❤️")

@client.on(events.NewMessage(outgoing=True, pattern=r"\.kon"))
async def love_msg(event):
    await event.edit("mai to simple si normal si ladki hu 🥺")

@client.on(events.NewMessage(outgoing=True, pattern=r"\.love"))
async def love_animation(event):
    frames = [
        "🤍",
        "💛",
        "🧡",
        "❤️",
        "💖",
        "💞",
        "💕",
        "💘 I Love You 💘"
    ]

    for frame in frames:
        await event.edit(frame)
        await asyncio.sleep(0.5)

@client.on(events.NewMessage(outgoing=True, pattern=r"\.pay"))
async def send_qr(event):
    await client.send_file(
        event.chat_id,
        "qr.jpg",
        caption="scan and pay karo"
    )
    await event.delete()

async def main():
    await client.start()
    print("Userbot running...")
    await client.run_until_disconnected()

keep_alive()
with client:
    client.loop.run_until_complete(main())
