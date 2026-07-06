import os
from pyrogram import Client, filters

# بيانات الحساب (استخدمها كما هي)
api_id = 37664645
api_hash = "f103f3863b43959a18fe5b21b191f43f"

# قراءة الجلسة من المتغيرات التي أضفتها في Railway
session_string = os.environ.get("SESSION_STRING")

# تشغيل البوت باستخدام الجلسة المحفوظة
app = Client("my_hunter_bot", api_id=api_id, api_hash=api_hash, session_string=session_string)

@app.on_message(filters.all)
async def hunter(client, message):
    text = message.text or message.caption or ""
    # فلتر صيد الهدايا
    if "t.me/" in text and any(k in text for k in ["Stars", "⭐️", "Price", "Gift"]):
        await message.forward("@Giftsao")
        print("تم صيد هدية!")

app.run()
