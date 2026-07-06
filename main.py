import logging
from telegram.ext import ApplicationBuilder, MessageHandler, filters

# 1. إعداد سجلات احترافية لمراقبة الأداء
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

TOKEN = "8674719543:AAG-9SeZarQsWiRWGn2u8Gg2ZQCg01UpZ-U"
MY_CHANNEL = "@Giftsao" 

# 2. وظيفة صيد الهدايا الذكية
async def hunt_gifts(update, context):
    if update.channel_post:
        msg = update.channel_post
        text = (msg.text or msg.caption or "").lower()
        
        # فلتر متقدم: لا يكتفي برابط، بل يبحث عن كلمات محفزة للسرعة
        keywords = ["price", "stars", "⭐️", "gift", "هدي", "سعر"]
        
        if "t.me/" in text and any(k in text for k in keywords):
            try:
                # إعادة توجيه الهدية فوراً
                await msg.forward(chat_id=MY_CHANNEL)
                # إضافة رسالة تأكيد في السجلات
                logging.info(f"تم صيد هدية بنجاح من: {msg.chat.title}")
            except Exception as e:
                logging.error(f"فشل في صيد الهدية: {e}")

if __name__ == '__main__':
    # 3. بناء البوت مع تحسينات الأداء (Concurrency)
    # نستخدم build() لضمان استقرار المهام
    app = ApplicationBuilder().token(TOKEN).concurrent_updates(True).build()
    
    # 4. معالج مخصص للقنوات فقط لتقليل الضغط على البوت
    app.add_handler(MessageHandler(filters.ChatType.CHANNEL, hunt_gifts))
    
    print("--- [ النظام يعمل بكفاءة عالية ] ---")
    print("--- [ الصياد يراقب القنوات الآن 24/7 ] ---")
    app.run_polling()
                
