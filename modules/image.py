import os
import aiogram
import modules.data as m_data
async def image(name,message:aiogram.types.Message,text = "picture",reply_markup=None):
    print(message.from_user.first_name)
    path = os.path.abspath(__file__+"/.."+"/.."+"/Images"+f"/{name}")
    file = aiogram.types.input_file.FSInputFile(path)
    id  = message.chat.id
    print(id)
    if reply_markup == None:

        await message.answer_photo(file)
    else:
        await message.answer_photo(reply_markup=reply_markup,photo=file)
    return file
    # m_data.bot.send_photo(chat_id=id,photo=file,caption=text)