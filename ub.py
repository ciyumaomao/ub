from telethon import TelegramClient, events

api_id = 20900277
api_hash = "6a3d761f9be590be4259404f34a1f81e"

client = TelegramClient("userbot_session", api_id, api_hash)

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    if event.is_private:
        message = event.raw_text.lower()
        if message == "hi":
            await event.reply("service?")

print("Userbot is running...")
client.start()
client.run_until_disconnected()
