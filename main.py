# -*- coding: utf-8 -*-
import logging
import re
import asyncio
import sys
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

logging.basicConfig(level=logging.INFO, stream=sys.stdout)

BOT_TOKEN = "8674719543:AAG-9SeZarQsWiRWGn2u8Gg2ZQCg01UpZ-U"
MY_CHANNEL = "@Giftsao"          
SOURCE_CHANNEL = "ResellGifts" # بدون @

gifts_queue = asyncio.Queue()

def get_star_price(text):
    match = re.search(r'(?:Price:|\u2b50\ufe0f)\s*(\d+)', text, re.IGNORECASE)
    return int(match.group(1)) if match else None

async def catch_live_gifts(update, context):
    if update.channel_post and update.channel_post.chat.username == SOURCE_CHANNEL:
        post_text = update.channel_post.text or ""
        price = get_star_price(post_text)
        
        if price and (400 <= price <= 600):
            gift_url = None
            if update.channel_post.reply_markup:
                for row in update.channel_post.reply_markup.inline_keyboard:
                    for button in row:
                        if button.url and "t.me/" in button.url:
                            gift_url = button.url
                            break
            if gift_url:
                await gifts_queue.put((post_text, gift_url, price))

async def continuous_publisher(app):
    while True:
        post_text, gift_url, price = await gifts_queue.get()
        btn = InlineKeyboardMarkup([[InlineKeyboardButton(f"الشراء مقابل ⭐️ {price}", url=gift_url)]])
        try:
            await app.bot.send_message(chat_id=MY_CHANNEL, text=f"🎁 هدية جديدة: ⭐️ {price}\n{gift_url}", reply_markup=btn)
        except Exception as e:
            print(f"Error: {e}")
        await asyncio.sleep(5)
        gifts_queue.task_done()

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.ChatType.CHANNEL, catch_live_gifts))
    app.job_queue.run_repeating(lambda c: None, interval=1) # تشغيل وهمي لبقاء الرابط
    
    loop = asyncio.get_event_loop()
    loop.create_task(continuous_publisher(app))
    app.run_polling()
        
