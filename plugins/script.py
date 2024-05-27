from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Translation(object):

    START_TEXT = """
𝐇𝐄𝐋𝐋𝐎 {} 😍👋,
𝗦𝗲𝗹𝗲𝗰𝘁 𝗧𝗵𝗲 𝗚𝗥𝗢𝗨𝗣 𝗬𝗢𝗨 𝗪𝗔𝗡𝗧🌺‼️

__**നിങ്ങൾക് ഇഷ്ടമുള്ള ഗ്രുപ്പ് select ചെയ്യുക.!!!**__
"""
    DETAILS_TEXT = """
**Hello {} 🫦
 
» രോമാഞ്ചം പ്രീമിയം 🔕

✅ • Daily Videos Updated
✅ • iOS supported
✅ • Full Direct Videos
✅ • Rare Collections & Hot Collections
✅ • Mallu aunty, Girls, etc… available 


🔞Many More Features 👍🏻

Price: 100

Click Pay Button, Pay The Amount And JOIN 🫦**
"""
    ABOUT_TEXT = """
**Mʏ ɴᴀᴍᴇ** : [ᴜᴘʟᴏᴀᴅᴇʀ ʙᴏᴛ ᴠ4](https://t.me/UploadLinkToFileBot)

**Sᴏᴜʀᴄᴇ** : [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://github.com/LISA-KOREA/UPLOADER-BOT-V4)

**Dᴀᴛᴀʙᴀsᴇ** : [MᴏɴɢᴏDB](https://cloud.mongodb.com)

**Lᴀɴɢᴜᴀɢᴇ :** [Pʏᴛʜᴏɴ 3.12.3](https://www.python.org/)

**Fʀᴀᴍᴇᴡᴏʀᴋ :** [ᴘʏʀᴏɢᴀᴍ 2.0.106](https://docs.pyrogram.org/)

**Dᴇᴠᴇʟᴏᴘᴇʀ :** @Luffy
"""


    PROGRESS = """
🏎️ Sᴘᴇᴇᴅ : {3}/s\n\n
✅ Dᴏɴᴇ : {1}\n\n
🟰 Tᴏᴛᴀʟ sɪᴢᴇ  : {2}\n\n
⏳ Tɪᴍᴇ ʟᴇғᴛ : {4}\n\n
"""


    START_BUTTONS = InlineKeyboardMarkup(
        [[  
        InlineKeyboardButton('രോമാഞ്ചം പ്രീമിയം 🔕', callback_data='premium')
        ],[
        InlineKeyboardButton('⛔️ Cʟᴏsᴇ', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 ʜᴏᴍᴇ', callback_data='home'),
        InlineKeyboardButton('👨‍🚒 ᴀʙᴏᴜᴛ', callback_data='about')
        ],[
        InlineKeyboardButton('⛔️ ᴄʟᴏsᴇ', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 ʜᴏᴍᴇ', callback_data='home'),
        InlineKeyboardButton('❔ ʜᴇʟᴘ', callback_data='help')
        ],[
        InlineKeyboardButton('⛔️ ᴄʟᴏsᴇ', callback_data='close')
        ]]
    )
    BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('⛔️ ᴄʟᴏsᴇ', callback_data='close')
        ]]
    )
