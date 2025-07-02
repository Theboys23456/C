from pyrogram import Client, filters
from datetime import datetime
import pytz
import os

API_ID = int(os.environ.get("API_ID", 21567814))
API_HASH = os.environ.get("API_HASH", "cd7dc5431d449fd795683c550d7bfb7e")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8133680149:AAE-pf43UZ7Oe5KYNRR_CMNIASYxCAL4tA0")

bot = Client("report-bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@bot.on_message(filters.command("report") & filters.private)
async def report_handler(client, message):
    try:
        text = message.text.strip().split()
        if len(text) < 2:
            return await message.reply("⚠️ Usage:
`/report @channelusername`", quote=True)

        channel_username = text[1]
        chat = await client.get_chat(channel_username)
        messages = await client.get_chat_history_count(chat.id)
        date_fmt = "%d-%m-%Y %I:%M %p"
        last_msg = await client.get_history(chat.id, limit=1)
        last_date = last_msg[0].date.astimezone(pytz.timezone("Asia/Kolkata")).strftime(date_fmt)

        report = f"""📊 <b>Channel Report:</b> <code>{channel_username}</code>

👥 <b>Members:</b> {chat.members_count}
📝 <b>Total Messages:</b> {messages}
🗓️ <b>Last Message:</b> {last_date}

✅ <i>Auto-generated report</i>"""
        await message.reply(report, quote=True, parse_mode="html")
    except Exception as e:
        await message.reply(f"❌ Error: <code>{e}</code>", parse_mode="html", quote=True)

bot.run()
