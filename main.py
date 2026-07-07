import os
import logging
from pyrogram import Client

# تفعيل تسجيل الأخطاء بالتفصيل
logging.basicConfig(level=logging.INFO)

api_id = 37664645
api_hash = "f103f3863b43959a18fe5b21b191f43f"
session_string = os.environ.get("SESSION_STRING")

print("--- [جاري فحص حالة البوت] ---")

if not session_string:
    print("خطأ فادح: المتغير SESSION_STRING غير موجود في الإعدادات!")
else:
    print(f"تم العثور على SESSION_STRING بطول: {len(session_string)} حرف")
    try:
        app = Client("test_session", api_id=api_id, api_hash=api_hash, session_string=session_string)
        print("تم تهيئة العميل بنجاح، جاري الاتصال...")
        app.start()
        print("الاتصال ناجح! البوت يعمل الآن.")
        app.stop()
    except Exception as e:
        print(f"فشل الاتصال بسبب: {e}")
        
