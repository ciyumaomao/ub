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

api_id = 20900277
api_hash = "6a3d761f9be590be4259404f34a1f81e"
session = "1BVtsOIQBu8ROMVWUG0AF2rZU4triGdflYo28zN5YimAjaCVFmNkiIhSemhNc7YSSqzQYxgTwh9vTtfpMH8X-GSWtr0jMJ_A8yYUAReR0QWe5ZG1q8GslCjpIZE-N_FnN-uwQRZhpRh7p5G58qMniwuhs-U8gt-jhoh8sT4guCL-l4TnWfdj8sh055AShQV_dcbPRPXX6lis11HYGKZotjIl6OzZVdnVGNSrmJU2qvZ1Hgrhii6NTw6cnywzXU0b3R9KA0ILT6v-J35dv_xzTSPs4zC3pmuCpxcGyIvozgBzJxAHnzLE-zvtktD6rVnc2XaCssweNsKmHJk5cS2pHTqGQYYFACA8="

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

@client.on(events.NewMessage(outgoing=True, pattern=r"\.b"))
async def boost_msg(event):
    await event.edit("boost kardo ise t.me/swapping_wifegf?boost ❤️")

@client.on(events.NewMessage(outgoing=True, pattern=r"\.alive"))
async def alive_msg(event):
    await event.edit("I'm alive my queen.. ❤️")

@client.on(events.NewMessage(outgoing=True, pattern=r"\.pay"))
async def send_qr(event):
    await client.send_file(
        event.chat_id,
        "qr.jpg",
        caption="Scan and pay"
    )
    await event.delete()

async def main():
    await client.start()
    print("Userbot running...")
    await client.run_until_disconnected()

keep_alive()
with client:
    client.loop.run_until_complete(main())
