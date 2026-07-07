import os
from pyrogram import Client, filters

# بياناتك المدمجة في الكود
api_id = 37664645
api_hash = "f103f3863b43959a18fe5b21b191f43f"
# ملاحظة: التوكن 8674719543:AAG... خاص بالبوتات، 
# كود الـ Userbot يعتمد على SESSION_STRING الموجود في الـ Variables.

# قراءة الجلسة (يجب أن تضيفها في Railway في تبويب Variables)
session_string = os.environ.get("SESSION_STRING")

# تهيئة التطبيق
app = Client(
    "my_hunter_bot", 
    api_id=api_id, 
    api_hash=api_hash, 
    session_string=session_string
)

# معالج الصيد
@app.on_message(filters.all)
async def hunter(client, message):
    text = message.text or message.caption or ""
    
    # الفلتر: يبحث عن الهدايا في الرسائل
    if "t.me/" in text and any(k in text for k in ["Stars", "⭐️", "Price", "Gift"]):
        try:
            # إعادة التوجيه لقناتك @Giftsao
            await message.forward("@Giftsao")
            print(f"تم صيد هدية من القناة: {message.chat.title if message.chat else 'خاص'}")
        except Exception as e:
            print(f"خطأ في النشر: {e}")

# تشغيل البوت
if __name__ == "__main__":
    app.run()
    
