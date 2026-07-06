from pyrogram import Client

# بياناتك التي أرسلتها
api_id = 37664645
api_hash = "f103f3863b43959a18fe5b21b191f43f"
bot_token = "8674719543:AAG-9SeZarQsWiRWGn2u8Gg2ZQCg01UpZ-U"

# إنشاء البوت
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# هذا الجزء هو الأساسي للعمل
@app.on_message()
def main(client, message):
    # هنا سيتم الرد على أي رسالة تصل للبوت
    message.reply("البوت يعمل بنجاح على Railway!")

print("تم تشغيل البوت بنجاح!")
app.run()
