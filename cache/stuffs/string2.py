from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from config import (BOT_NAME, SUPPORT_GROUP, OWNER_USERNAME, BOT_USERNAME)


button1 = [
    [
        InlineKeyboardButton(text="◉ ᴜᴘᴅᴀᴛᴇꜱ", url=f"https://t.me/SILENT_BOTS"),
        InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ ◉", url=f"http://t.me/{BOT_USERNAME}?startgroup=true"),
    ],
    [
        InlineKeyboardButton(text="◉ ᴏᴡɴᴇʀ", url=f"https://t.me/{OWNER_USERNAME}"),
        InlineKeyboardButton(text="ꜱᴏᴜʀᴄᴇ ◉", callback_data="repo_k"),
    ],                
    [                    
        InlineKeyboardButton(text="◉ ʜᴇʟᴘ ɴᴅ ᴄᴏᴍᴍᴀɴᴅꜱ ◉", callback_data="help_"),
    ],
]


button2 = [
    [
        InlineKeyboardButton(text="◈ ʙᴀꜱɪᴄ", callback_data="basic_"),
        InlineKeyboardButton(text="ᴀᴅᴠᴀɴᴄᴇ ◈", callback_data="admin_cmd"),
    ],
    [
        InlineKeyboardButton(text="◈ ᴄʟᴏꜱᴇ", callback_data="close_"),
        InlineKeyboardButton(text="ʙᴀᴄᴋ ◈", callback_data="HOME"),
    ],
]



button3 = [
    [
        InlineKeyboardButton(text="◈ ꜱᴏᴜʀᴄᴇ", url="https://github.com/ItsmeHyper13/DevuMusic"),
        InlineKeyboardButton(text="ʙᴀᴄᴋ ◈", callback_data="HOME"),
    ],
]


button4 = [
    [
        InlineKeyboardButton(text="◈ ᴄʟᴏꜱᴇ", callback_data="close_"),
        InlineKeyboardButton(text="ʙᴀᴄᴋ ◈", callback_data="help_"),
    ],
]





