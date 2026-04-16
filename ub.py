import os
from telethon import TelegramClient, events
from telethon.sessions import StringSession

api_id = 20900277
api_hash = "6a3d761f9be590be4259404f34a1f81e"
session = "1BVtsOIQBu8ROMVWUG0AF2rZU4triGdflYo28zN5YimAjaCVFmNkiIhSemhNc7YSSqzQYxgTwh9vTtfpMH8X-GSWtr0jMJ_A8yYUAReR0QWe5ZG1q8GslCjpIZE-N_FnN-uwQRZhpRh7p5G58qMniwuhs-U8gt-jhoh8sT4guCL-l4TnWfdj8sh055AShQV_dcbPRPXX6lis11HYGKZotjIl6OzZVdnVGNSrmJU2qvZ1Hgrhii6NTw6cnywzXU0b3R9KA0ILT6v-J35dv_xzTSPs4zC3pmuCpxcGyIvozgBzJxAHnzLE-zvtktD6rVnc2XaCssweNsKmHJk5cS2pHTqGQYYFACA8="

client = TelegramClient(StringSession(session), api_id, api_hash)

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    if event.is_private and event.raw_text.lower() == "hi":
        await event.reply("hello")

async def main():
    await client.start()
    print("Userbot running...")
    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())
