import aiogram

def create_keyboard(keyboard = [["Hello"]]):
    keyboard_1 = []
    for row in keyboard:
        keyboard_2 = []
        for button in row:
            keyboard_2.append(aiogram.types.KeyboardButton(text=button))
        keyboard_1.append(keyboard_2)
    return aiogram.types.ReplyKeyboardMarkup(keyboard= keyboard_1)
inline_keyboard=aiogram.types.InlineKeyboardMarkup(inline_keyboard=[[
    aiogram.types.InlineKeyboardButton(text="BUY",callback_data="buy 0"),
    aiogram.types.InlineKeyboardButton(text="DECLINE",callback_data="decline")
]])
def create_inline_keyboard(inline_keyboard = [["Buy","Cancel"]]):
    keyboard_1 = []
    for row in inline_keyboard:
        inline_keyboard_2 = []
        for button in row:
            inline_keyboard_2.append(aiogram.types.InlineKeyboardButton(text=button,callback_data=button))
        keyboard_1.append(inline_keyboard_2)
    return aiogram.types.InlineKeyboardMarkup(inline_keyboard= keyboard_1)