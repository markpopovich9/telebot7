import aiogram.filters as filters
import aiogram
import asyncio
import os
import sqlite3
import modules.data as m_data
import modules.sqlite as m_sqlite
import modules.image as m_image
import modules.keyboard as m_keyboard
@m_data.dp.message(filters.CommandStart())
async def start(message:aiogram.types.Message):
    #m_data.user = message.chat.username
    # m_sqlite.add_column(name_column="burger",type_column="INTEGER",name_table=message.from_user.username)
    # m_sqlite.add_column(name_column="hotDog",type_column="INTEGER",name_table=message.from_user.username)
    await message.answer(text="Hello",reply_markup=m_keyboard.create_keyboard([["Адміністратор","Кліент"]]))
    # #await m_image.image("burger.jpg",message,reply_markup=m_keyboard.create_inline_keyboard())
# @m_data.dp.message()
# async def moderator(message:aiogram.types.Message):
#     if message.chat.id==m_data.moderator_id and m_data.list_admin!=[]:
#         if message.text == "accept":
#             id = m_data.list_admin[-1][-1]
#             m_sqlite.set_value(columns=(id,"test"),values=(m_data.users[id]["phone"],message.text),name_table="AdminPhone")
#             m_sqlite.set_value(columns=(id,"test"),values=(m_data.users[id]["email"],message.text),name_table="AdminEmail")
#             m_sqlite.set_value(columns=(id,"test"),values=(m_data.users[id]["password"],message.text),name_table="AdminPassword")
#             m_sqlite.set_value(columns=(id,"test"),values=(m_data.users[id]["username"],message.text),name_table="Administration")
#             await m_data.bot.send_message(id,"Ви зареєстровані")
#             del m_data.list_admin[-1]
#         elif message.text=="no accept":
#             await m_data.bot.send_message(id,"Ви не зареєстровані")
            
@m_data.dp.message()
async def continue_1(message:aiogram.types.Message):
    print(message.chat.id,m_data.moderator_id)
    if message.chat.id==m_data.moderator_id:
        id = str(m_data.list_admin[-1][-1])
        name=str(m_data.list_admin[-1][0])
        if message.text == "accept":
            m_sqlite.add_column(name,"TEXT","AdminPassword")
            m_sqlite.add_column(name,"TEXT","Administration")
            m_sqlite.add_column(name,"TEXT","AdminEmail")
            m_sqlite.add_column(name,"TEXT","AdminPhone")
            m_sqlite.data.commit()
            m_sqlite.set_value(columns=(name,"test"),values=(m_data.users[id]["phone"],message.text),name_table="AdminPhone")
            m_sqlite.set_value(columns=(name,"test"),values=(m_data.users[id]["email"],message.text),name_table="AdminEmail")
            m_sqlite.set_value(columns=(name,"test"),values=(m_data.users[id]["password"],message.text),name_table="AdminPassword")
            m_sqlite.set_value(columns=(name,"test"),values=(m_data.users[id]["username"],message.text),name_table="Administration")
            await m_data.bot.send_message(id,"Ви зареєстровані")
            del m_data.list_admin[-1]
            m_sqlite.data.commit()
        elif message.text=="no accept":
            await m_data.bot.send_message(id,"Ви не зареєстровані")
            del m_data.list_admin[-1]
    else:
        # print(message) 
        m_sqlite.cursor.execute(f"CREATE TABLE IF NOT EXISTS AdminPassword (INTEGER PRIMARY KEY,id)")
        m_sqlite.cursor.execute(f"CREATE TABLE IF NOT EXISTS AdminEmail (INTEGER PRIMARY KEY,id)")
        m_sqlite.cursor.execute(f"CREATE TABLE IF NOT EXISTS AdminPhone (INTEGER PRIMARY KEY,id)")
        m_sqlite.cursor.execute(f"CREATE TABLE IF NOT EXISTS Administration (INTEGER PRIMARY KEY,id)")
        m_sqlite.add_column("test","TEXT","AdminPassword")
        m_sqlite.add_column("test","TEXT","Administration")
        m_sqlite.add_column("test","TEXT","AdminEmail")
        m_sqlite.add_column("test","TEXT","AdminPhone")
        # m_sqlite.add_column(name_column="burger",type_column="INTEGER",name_table=message.from_user.username)
        # m_sqlite.add_column(name_column="hotDog",type_column="INTEGER",name_table=message.from_user.username)
        if m_data.reg[0]:
            if m_data.reg[1]== "username":
                m_data.reg = [True,"password"]
                # print(m_data.users[str(message.chat.id)]["username"])
                m_data.users[str(message.chat.id)]["username"]=message.text
                # m_sqlite.set_value(columns=(message.chat.username,"test"),values=(message.text,message.text),name_table="AdminPassword")
                await message.answer(text="Укажіть свії пароль")
            elif m_data.reg[1]=="password":
                m_data.reg = [True,"email"]
                m_data.users[str(message.chat.id)]["password"]=message.text
                # m_sqlite.set_value(columns=(message.chat.username,"test"),values=(message.text,message.text),name_table="AdminPassword")
                await message.answer(text="Укажіть свії електрону почту")
            elif m_data.reg[1]=="email":
                m_data.reg = [True,"phone"]
                m_data.users[str(message.chat.id)]["email"]=message.text
                # m_sqlite.set_value(columns=(message.chat.username,"test"),values=(message.text,message.text),name_table="AdminEmail")
                await message.answer(text="Укажіть свії номер телефону")
            elif m_data.reg[1]=="phone":
                m_data.reg = [False,None]
                m_data.users[str(message.chat.id)]["phone"]=message.text
                # m_sqlite.set_value(columns=(message.chat.username,"test"),values=(message.text,message.text),name_table="AdminPhone")
                
                await message.answer(text="Зачекайте підтвердження модератора")
                text=f"Людина {str(message.chat.first_name)} хоче стати адміном:\n"
                text+=f"\t username: {m_data.users[str(message.chat.id)]['username']}\n"
                text+=f"\t password: {m_data.users[str(message.chat.id)]['password']}\n"
                text+=f"\t email: {m_data.users[str(message.chat.id)]['email']}\n"
                text+=f"\t phone: {m_data.users[str(message.chat.id)]['phone']}"
                print(message.chat.first_name,message.chat.id,m_data.list_admin)
                m_data.list_admin+=[[message.chat.first_name,message.chat.id]]
                await m_data.bot.send_message(m_data.moderator_id,text,reply_markup=m_keyboard.create_keyboard([["accept","no accept"]]))
                # await m_data.bot.send_message(m_data.moderator_id,f"\t username: {m_data.users[message.chat.username]['username']}")
                # await m_data.bot.send_message(m_data.moderator_id,f"\t password: {m_data.users[message.chat.username]['password']}")
                # await m_data.bot.send_message(m_data.moderator_id,f"\t email: {m_data.users[message.chat.username]['email']}")
                # await m_data.bot.send_message(m_data.moderator_id,f"\t phone: {m_data.users[message.chat.username]['phone']}")
                # await message.answer(text="Ви зарегистрировани")
            
        else:
            if message.text=="Кліент":
                m_data.user="client"
                # await m_image.image("burger.jpg",message,reply_markup=m_keyboard.create_inline_keyboard())
            elif message.text=="Адміністратор":
                m_data.user="admin"
                await message.answer(text="Реєстрація або Авторизація",reply_markup=m_keyboard.create_keyboard([["Авторизація","Реєстрація"]]))
            elif message.text == "Реєстрація" and m_data.user == "admin":
                try:
                    print(m_sqlite.get_value(message.chat.username,"AdminPhone")[0][0])
                    if not m_sqlite.get_value(message.chat.username,"AdminPhone")[0][0]:
                        0//0
                    await message.answer(text="Администратор с даним ником уже существуєт")
                except:
                    m_sqlite.add_column(name_column=message.chat.username,type_column="TEXT",name_table="Administration")
                    m_sqlite.add_column(name_column=message.chat.username,type_column="TEXT",name_table="AdminPassword")
                    m_sqlite.add_column(name_column=message.chat.username,type_column="TEXT",name_table="AdminEmail")
                    m_sqlite.add_column(name_column=message.chat.username,type_column="TEXT",name_table="AdminPhone")
                    m_data.users[str(message.chat.id)]={"user":message.chat.username}
                    m_data.reg=[True,"username"]
                    # m_sqlite.set_value(columns=(message.chat.username,"test"),values=(message.chat.username,message.text),name_table="Administration")
                    await  message.answer(text="Укажіть свії ім'я пользивателя")
            elif message.text == "Авторизація":
                pass
        # await m_image.image("hotDog.jpg",message,reply_markup=m_keyboard.create_inline_keyboard())
# @m_data.dp.callback_query()
# async def call_back(callback:aiogram.types.callback_query.CallbackQuery):
#     m_sqlite.cursor.execute(f"CREATE TABLE IF NOT EXISTS {callback.message.chat.username} (INTEGER PRIMARY KEY,id)")
#     m_sqlite.add_column(name_column="burger",type_column="INTEGER",name_table=callback.message.chat.username)
#     m_sqlite.add_column(name_column="hotDog",type_column="INTEGER",name_table=callback.message.chat.username)
#     m_sqlite.add_column(name_column="ok",type_column="INTEGER",name_table=callback.message.chat.username)
#     print(callback.message.photo)
#     # 8266 - burger  AgACAgIAAxkDAAIBBGWuuJ0oMnJYwIpf95NkRpK35TbWAALt0jEbntNRSQHvDJ-4XD86AQADAgADcwADNAQ
#     # 5332 - hot-dog AgACAgIAAxkDAAIBAmWuuIXU9cUzyesDz2PqgdMbKnp8AAL30jEbntNRSWfv-yIKPsJNAQADAgADcwADNAQ
#     inline_keyboard =callback.message.reply_markup
#     if callback.data== "Accept":
#         print(callback.message.photo[0].file_size)
#         if callback.message.photo[0].file_size==1320:
#             product="burger"
#         else:
#             product="hotDog"
#         count=callback.message.reply_markup.inline_keyboard[0][0].callback_data.split()[1]
#         print(product,count)
#         m_sqlite.set_value(columns=(product,"ok"),values=(count,count),name_table=callback.message.chat.username)
#         m_sqlite.data.commit()
#         inline_keyboard.inline_keyboard[0][0].text="Buy"
#         inline_keyboard.inline_keyboard[0][0].callback_data="Buy 0"
#         del inline_keyboard.inline_keyboard[1]
#         await callback.message.edit_reply_markup(reply_markup=inline_keyboard,inline_message_id=callback.inline_message_id)
#     if 'Buy' in callback.data:
#         count = '1'
#         if 'Buy' != callback.data:
#             count = callback.data.split(' ')
#             print(count)
#             count = str(int(count[-1])+1)
#             print(type(count))
#         if len(inline_keyboard.inline_keyboard)==1:
#             inline_keyboard.inline_keyboard.append(m_keyboard.create_inline_keyboard([['Accept']]).inline_keyboard[0])
#         print('0'==count)
#         print(type(inline_keyboard))
#         print()
#         inline_keyboard.inline_keyboard[0][0].callback_data = f'Buy {count}'
#         inline_keyboard.inline_keyboard[0][0].text = f'Buy {count}'
#         await callback.message.edit_reply_markup(reply_markup=inline_keyboard,inline_message_id=callback.inline_message_id)
#     if 'Cancel' in callback.data:
#         inline_keyboard =callback.message.reply_markup
#         count = '0'
#         if 'Buy' != callback.message.reply_markup.inline_keyboard[0][0].callback_data:
#             count1 = callback.message.reply_markup.inline_keyboard[0][0].callback_data.split(' ')
#             print(count)
#             if int(count1[-1])>0:
#                 count = str(int(count1[-1])-1)

#             print(type(count))
            
#         print('0'==count)
#         print(type(inline_keyboard))
#         print()
#         inline_keyboard.inline_keyboard[0][0].callback_data = f'Buy {count}'
#         inline_keyboard.inline_keyboard[0][0].text = f'Buy {count}'
        
#         try:
#             await callback.message.edit_reply_markup(reply_markup=inline_keyboard,inline_message_id=callback.inline_message_id)
#         except:
#             print("Telegeram error")
    # if len(inline_keyboard)== 1:

    #     # inline_keyboard.append([aiogram.types.InlineKeyboardButton(text="accept",callback_data="accept")])
    #     # inline_keyboard[0][0].callback_data = 'buy 0'
        
    #     print(','.split(str(inline_keyboard)),str(inline_keyboard))#я за водой
    #     print('\n')
    #     print('\n')
    #     print('\n')
async def main():
    await m_data.dp.start_polling(m_data.bot)
asyncio.run(main())
m_sqlite.data.commit()
m_sqlite.data.close()