import aiogram
import asyncio
import aiogram.filters as filters
import os
import sqlite3
import modules.data as m_data
import modules.sqlite as m_sqlite
import modules.image as m_image
import modules.keyboard as m_keyboard
@m_data.dp.message(filters.CommandStart())
async def start(message:aiogram.types.Message):
    await message.answer(text="Hello",reply_markup=m_keyboard.create_inline_keyboard())
    await m_image.image("burger.jpg",message,reply_markup=m_keyboard.create_keyboard())
async def main():
    await m_data.dp.start_polling(m_data.bot)
asyncio.run(main())
m_sqlite.data.commit()
m_sqlite.data.close()