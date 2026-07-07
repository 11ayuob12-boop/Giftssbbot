import os
from pyrogram import Client

# بياناتك
api_id = 37664645
api_hash = "f103f3863b43959a18fe5b21b191f43f"

# قراءة الجلسة من متغيرات البيئة (هذا هو السر!)
session_string = os.environ.get("SESSION_STRING")

# تشغيل البوت
app = Client("my_bot", api_id=api_id, api_hash=api_hash, session_string=session_string)

@app.on_message()
async def main(client, message):
    print("تم استلام رسالة جديدة")

app.run()
