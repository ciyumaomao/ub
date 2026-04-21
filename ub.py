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

TARGET_GROUP_ID = -1003623091628
replied_users = set()
start_time = time.time()

# ---------------- 24x7 TYPING PRANK ---------------- #

async def fake_typing():
    while True:
        try:
            async with client.action(TARGET_GROUP_ID, 'typing'):
                await asyncio.sleep(random.randint(6, 12))
        except Exception as e:
            print("Typing Error:", e)
            await asyncio.sleep(15)

@client.on(events.NewMessage(incoming=True))
async def auto_reply(event):
    if event.is_private and not event.out:
        if event.raw_text.lower() in ["hi", "hello", "hii", "hey", "hyy", "hy"]:
            async with client.action(event.chat_id, 'typing'):
                await asyncio.sleep(random.randint(2,4))
            await event.reply('''🐣🦋 𝗦𝗘𝗥𝗩𝗜𝗖𝗘 𝗔𝗩𝗔𝗜𝗟𝗔𝗕𝗟𝗘 🐣🦋

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
    await event.edit("𝘽𝙊𝙊𝙎𝙏 𝙏𝙃𝙄𝙎 𝙂𝙍𝙊𝙐𝙋 💋 \nt.me/wife_swapping_gf?boost ❤️")

@client.on(events.NewMessage(outgoing=True, pattern=r"\.boostshiv"))
async def boost_msgg(event):
    await event.edit("𝘽𝙊𝙊𝙎𝙏 𝙏𝙃𝙄𝙎 𝘾𝙃𝘼𝙉𝙉𝙀𝙇 💋 \nt.me/thnxshiv?boost? ❤️")

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

@client.on(events.NewMessage(pattern=r"\.hack"))
async def hack_animation(event):
    steps = [
        "🟩 Initializing hack...",
        "🟩 Connecting to target...",
        "🟩 Bypassing firewall...",
        "🟩 Injecting payload...",
        "🟩 Accessing database...",
        "🟩 Downloading files...",
        "🟥 Trace detected...",
        "🟩 Trace bypassed...",
        "🟩 Access Granted!",
        "💀 Target successfully hacked!"
    ]

    msg = await event.respond("Starting...")
    
    for step in steps:
        await asyncio.sleep(1.2)
        await msg.edit(step)

@client.on(events.NewMessage(pattern=r"\.bar"))
async def progress_bar(event):
    msg = await event.respond("Starting...")

    frames = [
        "[□□□□□□□□□□] 10%",
        "[■■□□□□□□□□] 20%",
        "[■■■□□□□□□□] 30%",
        "[■■■■□□□□□□] 40%",
        "[■■■■■□□□□□] 50%",
        "[■■■■■■□□□□] 60%",
        "[■■■■■■■□□□] 70%",
        "[■■■■■■■■□□] 80%",
        "[■■■■■■■■■□] 90%",
        "[■■■■■■■■■■] 100%"
    ]

    for frame in frames:
        await asyncio.sleep(0.5)
        await msg.edit(frame)

    await msg.edit("✅ Completed!")

@client.on(events.NewMessage(pattern=r"\.type (.+)"))
async def type_text(event):
    text = event.pattern_match.group(1)
    msg = await event.respond("")

    current = ""
    for char in text:
        current += char
        await asyncio.sleep(0.1)
        await msg.edit(current)

@client.on(events.NewMessage(pattern=r"\.lovemeter"))
async def lovemeter(event):
    msg = await event.respond("Calculating love...")

    frames = [
        "❤️ [■□□□□□□□□□] 10%",
        "❤️ [■■□□□□□□□□] 20%",
        "❤️ [■■■□□□□□□□] 30%",
        "❤️ [■■■■□□□□□□] 40%",
        "❤️ [■■■■■□□□□□] 50%",
        "❤️ [■■■■■■□□□□] 60%",
        "❤️ [■■■■■■■□□□] 70%",
        "❤️ [■■■■■■■■□□] 80%",
        "❤️ [■■■■■■■■■□] 90%",
        "❤️ [■■■■■■■■■■] 100%",
        "💘 Love Confirmed!"
    ]

    for frame in frames:
        await asyncio.sleep(0.4)
        await msg.edit(frame)

@client.on(events.NewMessage(pattern=r"\.kiss"))
async def kiss(event):
    msg = await event.respond("😘")

    frames = [
        "😘",
        "😘💕",
        "😘💕💕",
        "😘💕💕💕",
        "💋 Sending Kiss..."
    ]

    for frame in frames:
        await asyncio.sleep(0.6)
        await msg.edit(frame)

@client.on(events.NewMessage(pattern=r"\.spam (\d+) (.+)"))
async def spam(event):
    count = int(event.pattern_match.group(1))
    text = event.pattern_match.group(2)

    await event.delete()  # removes your command message

    for _ in range(count):
        await event.respond(text)
        await asyncio.sleep(0.3)

@client.on(events.NewMessage(pattern=r"\.hug"))
async def hug(event):
    reply = await event.get_reply_message()
    if not reply:
        return await event.respond("Reply to someone to hug them 🤗")

    msg = await event.respond("Sending hug...")

    frames = [
        "🤗",
        "🤗💕",
        "🫂💖",
        "💖 Hug sent!"
    ]

    for frame in frames:
        await asyncio.sleep(0.7)
        await msg.edit(frame)

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
