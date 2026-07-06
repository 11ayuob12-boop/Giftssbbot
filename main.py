from pyrogram import Client, filters

# بياناتك
api_id = 37664645
api_hash = "f103f3863b43959a18fe5b21b191f43f"

# إنشاء الصياد
app = Client("my_hunter_bot", api_id=api_id, api_hash=api_hash)

# القناة التي تنشر فيها الهدايا (قناتك)
MY_CHANNEL = "@Giftsao"

@app.on_message(filters.channel)
async def hunter(client, message):
    text = message.text or message.caption or ""
    
    # فلتر البحث: هل الرسالة تحتوي رابط هدية؟ وهل بها نجوم؟
    # هذا الفلتر يبحث عن أي شيء يتعلق بالهدايا (Stars/Gifts)
    if "t.me/" in text and ("Stars" in text or "⭐️" in text or "Price" in text):
        try:
            # إعادة توجيه الهدية لقناتك بسرعة فائقة
            await message.forward(MY_CHANNEL)
            print(f"تم صيد هدية من: {message.chat.title}")
        except Exception as e:
            print(f"خطأ في الصيد: {e}")

print("الصياد في حالة استنفار.. يراقب كل القنوات!")
app.run()
                            
