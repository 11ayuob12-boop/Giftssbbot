import logging
from telegram.ext import ApplicationBuilder, MessageHandler, filters

# إعداد السجلات لتتبع الأخطاء
logging.basicConfig(level=logging.INFO)

# ضع التوكن الخاص بك هنا
TOKEN = "8674719543:AAG-9SeZarQsWiRWGn2u8Gg2ZQCg01UpZ-U"
MY_CHANNEL = "@Giftsao" # قناتك التي ستنشر فيها

async def handle_gift(update, context):
    # نتحقق إذا كانت الرسالة من قناة مصدر
    if update.channel_post:
        text = update.channel_post.text or ""
        # بحث عن أي رابط تليجرام وأي كلمات دلالية للهدايا
        if "t.me/" in text and any(word in text for word in ["Price", "Stars", "⭐️"]):
            try:
                # إعادة توجيه الهدية لقناتك
                await update.channel_post.forward(chat_id=MY_CHANNEL)
                print("تم التقاط هدية جديدة بنجاح!")
            except Exception as e:
                print(f"خطأ أثناء النشر: {e}")

if __name__ == '__main__':
    # بناء التطبيق بدون الحاجة لـ job_queue
    app = ApplicationBuilder().token(TOKEN).build()
    
    # إضافة المعالج (الذي يراقب القنوات التي تضعه فيها)
    app.add_handler(MessageHandler(filters.ChatType.CHANNEL, handle_gift))
    
    print("البوت يعمل الآن ومستعد للصيد...")
    app.run_polling()
    
