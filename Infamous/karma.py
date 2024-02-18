# https://github.com/Infamous-Hydra/YaeMiko
# https://github.com/Team-ProjectCodeX
# https://t.me/O_okarma

# <============================================== IMPORTS =========================================================>
from pyrogram.types import InlineKeyboardButton as ib
from telegram import InlineKeyboardButton

from Mikobot import BOT_USERNAME, OWNER_ID, SUPPORT_CHAT

# <============================================== CONSTANTS =========================================================>
FIRST_PART_TEXT = "💓"

PM_START_TEXT = "*ʜᴇʏ ɪ ᴀᴍ ᴀʟɪᴠᴇ ʙᴀʙʏ*"

GROUP_START_BTN = [
    [
        InlineKeyboardButton(
            text="𝗛𝗜𝗝𝗔𝗖𝗞 𝗠𝗘",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="𝗦𝗨𝗣𝗣𝗢𝗥𝗧", url=f"https://t.me/{SUPPORT_CHAT}"),
        InlineKeyboardButton(text="𝗖𝗥𝗘𝗔𝗧𝗢𝗥", url=f"tg://user?id={OWNER_ID}"),
    ],
]

ALIVE_BTN = [
    [
        ib(text="𝗦𝗨𝗣𝗣𝗢𝗥𝗧", url="https://t.me/savage_networks"),
    ],
    [
        ib(
            text="𝗛𝗜𝗝𝗔𝗖𝗞 𝗠𝗘⚡",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
]

HELP_STRINGS = """
🌷 *ᴍᴀɴᴀɢᴍᴇɴᴛ ᴄᴏᴍᴍᴀɴᴅꜱ* 🌷

☉ *Here, you will find a list of all the available commands.*

ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ : /
"""
