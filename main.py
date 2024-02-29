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
    
    # await m_data.bot.send_photo(chat_id=-1002018580317,photo= "AgACAgIAAxkBAAIIlGXTnD7A3y9I20yYBj-kW_QGUTcqAAIw1jEbHNqhSs55BHrdiYNbAQADAgADeQADNAQ")
    # if message.chat.id==m_data.moderator_id:

    #     id = str(m_data.list_admin[-1][-1])
    #     name=str(m_data.list_admin[-1][0])
    #     if message.text == "Прийняти":
    #         name=m_data.users[id]['username']
    #         m_sqlite.cursor.execute(f"CREATE TABLE IF NOT EXISTS Admin_{name} (INTEGER PRIMARY KEY,id)")
    #         m_sqlite.add_column("username","TEXT",f"Admin_{name}")
    #         m_sqlite.add_column("password","TEXT",f"Admin_{name}")
    #         m_sqlite.add_column("email","TEXT",f"Admin_{name}")
    #         m_sqlite.add_column("phone","TEXT",f"Admin_{name}")
    #         m_sqlite.data.commit()
    #         m_sqlite.set_value(columns=(
    #                                     "username",
    #                                     "password",
    #                                     "email",
    #                                     "phone"),
    #                            values=(
    #                                 m_data.users[id]["username"],
    #                                 m_data.users[id]["password"],
    #                                 m_data.users[id]["email"],
    #                                 m_data.users[id]["phone"],
    #                                 ),
    #                            name_table= f"Admin_{name}")

        
    #         # m_sqlite.set_value(columns=("i"+id,"test"),values=(m_data.users[id]["phone"],message.text),name_table="AdminPhone")
    #         # m_sqlite.set_value(columns=("i"+id,"test"),values=(m_data.users[id]["email"],message.text),name_table="AdminEmail")
    #         # m_sqlite.set_value(columns=("i"+id,"test"),values=(m_data.users[id]["password"],message.text),name_table="AdminPassword")
    #         # m_sqlite.set_value(columns=("i"+id,"test"),values=(m_data.users[id]["username"],message.text),name_table="Administration")
            
    #         await m_data.bot.send_message(id,"Ви зареєстровані",reply_markup=m_keyboard.create_keyboard([["Додати продукт","Надіслати повідомлення"]]))
    #         await message.answer(f"адміністратор {m_data.users[id]['username']} зареєстрований")
    #         del m_data.list_admin[-1]
    #         m_sqlite.data.commit()
    #     elif message.text=="Відхилити":
    #         await m_data.bot.send_message(id,"Ви не зареєстровані")
    #         del m_data.list_admin[-1]
    
    if True:
        name_1="None"
        if message.chat.username != None:
            name_1=message.chat.username
        elif message.chat.first_name != None:
            name_1=message.chat.first_name
        elif message.chat.last_name != None:
            name_1=message.chat.last_name
        # else:
        #     name_1
        name = name_1.split(" ")
        name = "_".join(name)
        try:
            print(m_data.dict_admin[f"{message.chat.id}"])
            if m_data.dict_admin[f"{message.chat.id}"][0]:
                if message.text == "Відправити повідомлення" and m_data.dict_admin[f"{message.chat.id}"][1]["status"]==None:
                    await message.answer(text="Вкажіть текст сповіщення")
                    m_data.dict_admin[f"{message.chat.id}"][1]["status"]="text"
                elif  m_data.dict_admin[f"{message.chat.id}"][1]["status"]=="text":
                    await message.answer(text="Вкажіть опис повідомлення")
                    m_data.dict_admin[f"{message.chat.id}"][1]["status"]="description1"
                    m_data.dict_admin[f"{message.chat.id}"][1]["text"]=message.text
                elif m_data.dict_admin[f"{message.chat.id}"][1]["status"]=="description1":
                    # inline_keyboard = aiogram.types.InlineKeyboardMarkup(inline_keyboard=[[
                    #         aiogram.types.InlineKeyboardButton(text="INFO",callback_data="buy 0"),
                    #         aiogram.types.InlineKeyboardButton(text="BUY",callback_data="decline")
                    #     ],
                    #     [
                    #         aiogram.types.InlineKeyboardButton(text="")
                    #     ] 
                    # ])
                    # # [[1,2][8]]
                    # await message.answer(text=m_data.dict_admin[f"{message.chat.id}"][1]["text"])
                    await message.answer(text="Зараз ще не готово")
                if message.text == "Додати продукт" and m_data.dict_admin[f"{message.chat.id}"][1]["status"]==None:
                    await message.answer(text="Вкажіть назву продукту")
                    m_data.dict_admin[f"{message.chat.id}"][1]["status"]="name"
                elif m_data.dict_admin[f"{message.chat.id}"][1]["status"]=="name":
                    await message.answer(text="Вкажіть опис продукту")
                    m_data.dict_admin[f"{message.chat.id}"][1]["status"]="description"
                    m_data.dict_admin[f"{message.chat.id}"][1]["name"]=message.text
                elif "description" == m_data.dict_admin[f"{message.chat.id}"][1]["status"]:
                    # print(m_data.dict_admin[f"{message.chat.id}"][1].split("_descriptio"))
                    m_data.dict_admin[f"{message.chat.id}"][1]["status"]="image"
                    m_data.dict_admin[f"{message.chat.id}"][1]["description"]=message.text
                    # m_sqlite.add_product(m_data.dict_admin[f"{message.chat.id}"][1].split("_descriptio")[0],message.text,os.path.abspath(__file__+"/../Images/burger.jpg"))
                    
                    await message.answer(text="Відправте зображення")
                elif m_data.dict_admin[f"{message.chat.id}"][1]["status"]== "image":
                    print()
                    print(message.document)
                    print()
                    
                    image_id = None
                    if message.photo != None:
                        image_id =message.photo[-1].file_id
                    #elif message.document != None:
                    #   image_id =message.document.thumbnail.file_id
                    # BQACAgIAAxkBAAIGDWXKZZRdBDCew0ozMxutds2LzwwWAALcRwACSpdQShMSmeSP9TyxNAQ
                    # AgACAgIAAxkBAAIGImXKZgGc32A7myq6jhJnUjvjIGRkAAIN2jEbSpdQSg4LLB8ljT0rAQADAgADeQADNAQ
                    if image_id != None:
                        #await message.answer_photo(image_id)
                        print(111)
                        m_sqlite.add_product(
                            m_data.dict_admin[f"{message.chat.id}"][1]["name"],
                            m_data.dict_admin[f"{message.chat.id}"][1]["description"],
                            image_id,
                            message
                        )
                        print(113)
                        await message.answer(text="Продукт знаходиться в базі данних\nприклад продукту:")
                        inline_keyboard=m_keyboard.inline_keyboard
                        inline_keyboard.inline_keyboard[0][0].callback_data+=f" {m_data.dict_admin[f'{message.chat.id}'][1]['name']}"
                        await message.answer_photo(image_id,reply_markup=m_keyboard.inline_keyboard)
                        # -1002018580317
                        print(115)
                        print(image_id)
                        await m_data.bot.send_photo(chat_id=-1002018580317,photo= image_id,reply_markup= m_keyboard.inline_keyboard)
                        print(116)
                    else:
                        await message.answer(text="Ви відіслали не зображення")
                    print(image_id)
            print('hi','hello')
        except:
            
        # m_data.dict_users[message.chat.id]=[message.chat.username,message.chat.first_name,message.chat.last_name,name]
        
        # m_sqlite.cursor.execute(f"CREATE TABLE IF NOT EXISTS AdminPassword (INTEGER PRIMARY KEY,id)")
        # m_sqlite.cursor.execute(f"CREATE TABLE IF NOT EXISTS AdminEmail (INTEGER PRIMARY KEY,id)")
        # m_sqlite.cursor.execute(f"CREATE TABLE IF NOT EXISTS AdminPhone (INTEGER PRIMARY KEY,id)")
        # m_sqlite.cursor.execute(f"CREATE TABLE IF NOT EXISTS Administration (INTEGER PRIMARY KEY,id)")
        # m_sqlite.add_column("test","TEXT","AdminPassword")
        # m_sqlite.add_column("test","TEXT","Administration")
        # m_sqlite.add_column("test","TEXT","AdminEmail")
        # m_sqlite.add_column("test","TEXT","AdminPhone")
        # m_sqlite.add_column(name_column="burger",type_column="INTEGER",name_table=message.from_user.username)
        # m_sqlite.add_column(name_column="hotDog",type_column="INTEGER",name_table=message.from_user.username)
            if m_data.reg[0]:
                if m_data.reg[1]== "username":
                    try:
                        print(m_sqlite.get_value(name_table=f"Admin_{message.text}"))
                        await message.answer(text="Користувач с таким ніком вже існує")
                    except:
                        m_data.reg = [True,"password"]
                        # print(m_data.users[str(message.chat.id)]["username"])
                    m_data.users[str(message.chat.id)]["username"]=message.text
                    # m_sqlite.set_value(columns=(message.chat.username,"test"),values=(message.text,message.text),name_table="AdminPassword")
                    await message.answer(text="Укажіть свій пароль")
                elif m_data.reg[1]=="password":
                    m_data.reg = [True,"email"]
                    m_data.users[str(message.chat.id)]["password"]=message.text
                    # m_sqlite.set_value(columns=(message.chat.username,"test"),values=(message.text,message.text),name_table="AdminPassword")
                    await message.answer(text="вкажіть свою електронну пошту")
                elif m_data.reg[1]=="email":
                    m_data.reg = [True,"phone"]
                    m_data.users[str(message.chat.id)]["email"]=message.text
                    # m_sqlite.set_value(columns=(message.chat.username,"test"),values=(message.text,message.text),name_table="AdminEmail")
                    await message.answer(text="Укажіть свій номер телефону")
                elif m_data.reg[1]=="phone":
                    m_data.reg = [False,None]
                    m_data.users[str(message.chat.id)]["phone"]=message.text
                    # m_sqlite.set_value(columns=(message.chat.username,"test"),values=(message.text,message.text),name_table="AdminPhone")
                    
                    await message.answer(text="Зачекайте підтвердження модератора")
                    text=f"Людина {m_data.users[str(message.chat.id)]['username']} хоче стати адміном:\n"
                    text+=f"\t username: {m_data.users[str(message.chat.id)]['username']}\n"
                    text+=f"\t password: {m_data.users[str(message.chat.id)]['password']}\n"
                    text+=f"\t email: {m_data.users[str(message.chat.id)]['email']}\n"
                    text+=f"\t phone: {m_data.users[str(message.chat.id)]['phone']}\n"
                    text +=f"Телеграм дані:\n"
                    text += f"\t username: {message.chat.username}\n"
                    text += f"\t first name: {message.chat.first_name}\n"
                    text += f"\t last name: {message.chat.last_name}"
                    # print(message.chat.first_name,message.chat.id,m_data.list_admin)
                    # m_data.list_admin+=[[name,message.chat.id]]
                    # print(m_data.users[message.chat.id]['usename'])
                    m_data.list_admin[f"{m_data.users[f'{message.chat.id}']['username']}"] = True
                    inline_keyboard=aiogram.types.InlineKeyboardMarkup(inline_keyboard=[[
                        aiogram.types.InlineKeyboardButton(text="Прийняти",callback_data=f"accept_{message.chat.id}_True"),
                        aiogram.types.InlineKeyboardButton(text="Відхилити",callback_data=f"reject_{message.chat.id}_True")
                    ]])
                    await m_data.bot.send_message(m_data.moderator_id,text,reply_markup=inline_keyboard)
                    # await m_data.bot.send_message(m_data.moderator_id,f"\t username: {m_data.users[message.chat.username]['username']}")
                    # await m_data.bot.send_message(m_data.moderator_id,f"\t password: {m_data.users[message.chat.username]['password']}")
                    # await m_data.bot.send_message(m_data.moderator_id,f"\t email: {m_data.users[message.chat.username]['email']}")
                    # await m_data.bot.send_message(m_data.moderator_id,f"\t phone: {m_data.users[message.chat.username]['phone']}")
                    # await message.answer(text="Ви зарегистрировани")
            else:
                try:
                    if m_data.autoriz[str(message.chat.id)] != None:
                        if m_data.autoriz[str(message.chat.id)] == "username":
                            try:
                                m_sqlite.get_value(name_table="Admin_"+message.text)
                                
                                m_data.users[str(message.chat.id)]= {"username":message.text}
                                await message.answer(text="Укажіть свій пароль")
                                m_data.autoriz[str(message.chat.id)]="password"
                            except:
                                await message.answer(text="адміна з даним ніком не існує")#так существует или нет
                        elif m_data.autoriz[str(message.chat.id)] == "password":
                            data = lambda column: m_sqlite.get_value(
                                column=column,
                                name_table="Admin_"+m_data.users[str(message.chat.id)]["username"]
                            )
                            print(data("password"))
                            if data("password")==message.text:
                                m_data.users[f"{message.chat.id}"]["email"] = data("email") 
                                m_data.users[f"{message.chat.id}"]["phone"] = data("phone")
                                m_data.autoriz[str(message.chat.id)] = None
                                m_data.dict_admin[str(message.chat.id)]= [True,{"status": None}]
                                await message.answer(text="Ви були авторезовані",reply_markup=m_keyboard.create_keyboard([["Додати продукт","Надіслати повідомлення"]]))
                            else:
                                await message.answer(text="Пароль не вірний ")
                            
                    else:
                        0/0
                except: 
                
                        if message.text=="Кліент":
                            m_data.user="client"
                            # await m_image.image("burger.jpg",message,reply_markup=m_keyboard.create_inline_keyboard())
                        elif message.text=="Адміністратор":
                            m_data.user="admin"
                            await message.answer(text="Реєстрація або Авторизація",reply_markup=m_keyboard.create_keyboard([["Авторизація","Реєстрація"]]))
                        elif message.text == "Реєстрація" and m_data.user == "admin":
                            # try:
                            #     # print(m_sqlite.get_value(message.chat.username,"AdminPhone")[0][0])
                            #     if not m_sqlite.get_value(message.chat.username,f"Admin_{name}")[0][0]:
                            #         0//0
                            #     await message.answer(text="Адміністратор з цим ником вже існує")
                            # except:
                                # m_sqlite.add_column(name_column=message.chat.username,type_column="TEXT",name_table="Administration")
                                # m_sqlite.add_column(name_column=message.chat.username,type_column="TEXT",name_table="AdminPassword")
                                # m_sqlite.add_column(name_column=message.chat.username,type_column="TEXT",name_table="AdminEmail")
                                # m_sqlite.add_column(name_column=message.chat.username,type_column="TEXT",name_table="AdminPhone")
                                m_data.users[str(message.chat.id)]={"user":message.chat.username}
                                m_data.reg=[True,"username"]
                                # m_sqlite.set_value(columns=(message.chat.username,"test"),values=(message.chat.username,message.text),name_table="Administration")
                                await message.answer(text="вкажіть ім'я користувача")
                        elif message.text == "Авторизація":
                            await message.answer(text="Укажіть свій нік")
                            m_data.autoriz[str(message.chat.id)]="username"
                        
            # await m_image.image("hotDog.jpg",message,reply_markup=m_keyboard.create_inline_keyboard())
@m_data.dp.callback_query()
async def call_back(callback:aiogram.types.callback_query.CallbackQuery):
    message = callback.message
    # -1002018580317
    if message.photo!= None:
        if "buy" in callback.data:
            data = callback.data.split(" ")
            reply_markup= message.reply_markup
            
            if len(reply_markup.inline_keyboard)==1:
                reply_markup.inline_keyboard.append([aiogram.types.inline_keyboard_button.InlineKeyboardButton(text="accept",callback_data="accept")])
            data[1]=str(int(data[1])+1)
            reply_markup.inline_keyboard[0][0].callback_data=" ".join(data)
            reply_markup.inline_keyboard[0][0].text= data[0]+" "+data[1]
            await message.edit_reply_markup(callback.inline_message_id,reply_markup)
        elif "decline" in callback.data:
            reply_markup= message.reply_markup
            data=reply_markup.inline_keyboard[0][0].callback_data.split(" ")
            if data[1]!="0":
                data[1]=str(int(data[1])-1)
                reply_markup.inline_keyboard[0][0].callback_data=" ".join(data)
                reply_markup.inline_keyboard[0][0].text= data[0]+" "+data[1]
                if data[1]=="0":
                    reply_markup=m_keyboard.inline_keyboard
                    reply_markup.inline_keyboard[0][0].callback_data+=f" {data[2]}"
                await message.edit_reply_markup(callback.inline_message_id,reply_markup)
        elif "accept" in callback.data:
            try:
                name_table = f"Basket_{m_data.users[f'{callback.from_user.id}']['username']}"
                print(name_table)
                
                data=message.reply_markup.inline_keyboard[0][0].callback_data.split(" ")
                inline_keyboard=m_keyboard.inline_keyboard
                inline_keyboard.inline_keyboard[0][0].callback_data+=f" {data[2]}"
                print(callback.from_user)
                m_sqlite.cursor.execute(f"CREATE TABLE IF NOT EXISTS {name_table} (INTEGER PRIMARY KEY,id)")
                m_sqlite.add_column("chat_id","TEXT",name_table)
                m_sqlite.add_column("count","INTEGER", name_table)
                m_sqlite.add_column("product","TEXT",name_table)
                m_sqlite.add_column("email","TEXT",name_table)
                m_sqlite.add_column("phone","TEXT",name_table)
                m_sqlite.set_value(
                    ("chat_id","count","product",'email','phone'),
                    [
                        callback.from_user.id,
                        int(data[1]),
                        data[2],
                        m_data.users[f'{callback.from_user.id}']['email'],
                        m_data.users[f'{callback.from_user.id}']['phone'],
                    ],
                    name_table=name_table
                )
                m_sqlite.data.commit()
                await message.edit_reply_markup(callback.inline_message_id,inline_keyboard)
            except:
                await m_data.bot.send_message(callback.from_user.id,"Вам потрібно зареєструватись або авторизуватись для покупки товарів", reply_markup= m_keyboard.create_keyboard([["Адміністратор","Кліент"]]))
    elif message.chat.id==m_data.moderator_id:
        
        
        # try:
            print(callback.data)
            list= callback.data.split("_")
            id = list[1]
            # name= list[1]
            can=list[-1]
            print(can)
            print(bool("False"))
            if list[0] == "accept" and can == "True":
                
                name=m_data.users[id]['username']
                m_sqlite.cursor.execute(f"CREATE TABLE IF NOT EXISTS Admin_{name} (INTEGER PRIMARY KEY,id)")
                m_sqlite.add_column("username","TEXT",f"Admin_{name}")
                m_sqlite.add_column("password","TEXT",f"Admin_{name}")
                m_sqlite.add_column("email","TEXT",f"Admin_{name}")
                m_sqlite.add_column("phone","TEXT",f"Admin_{name}")
                m_sqlite.data.commit()
                m_sqlite.set_value(columns=(
                                            "username",
                                            "password",
                                            "email",
                                            "phone"),
                                values=(
                                        m_data.users[id]["username"],
                                        m_data.users[id]["password"],
                                        m_data.users[id]["email"],
                                        m_data.users[id]["phone"],
                                        ),
                                name_table= f"Admin_{name}")


                # m_sqlite.set_value(columns=("i"+id,"test"),values=(m_data.users[id]["phone"],message.text),name_table="AdminPhone")
                # m_sqlite.set_value(columns=("i"+id,"test"),values=(m_data.users[id]["email"],message.text),name_table="AdminEmail")
                # m_sqlite.set_value(columns=("i"+id,"test"),values=(m_data.users[id]["password"],message.text),name_table="AdminPassword")
                # m_sqlite.set_value(columns=("i"+id,"test"),values=(m_data.users[id]["username"],message.text),name_table="Administration")
                
                await m_data.bot.send_message(id,"Ви зареєстровані",reply_markup=m_keyboard.create_keyboard([["Додати продукт","Надіслати повідомлення"]]))
                await message.answer(f"адміністратор {m_data.users[id]['username']} зареєстрований")
                m_sqlite.data.commit()
                m_data.dict_admin[id]= [True,{"status": None}]
                # m_data.list_admin[f"{m_data.users[f'{message.chat.id}']['username']}"] = False
            elif list[0]=="reject" and can == "True":

                await m_data.bot.send_message(id,"Ви не зареєстровані")
                # m_data.list_admin[f"{m_data.users[f'{message.chat.id}']['username']}"] = False
            del list[-1]
            inline_keyboard=message.reply_markup
            inline_keyboard.inline_keyboard[0][0].callback_data = "_".join(list)
            inline_keyboard.inline_keyboard[0][1].callback_data = "_".join(list)
            await message.edit_reply_markup(callback.inline_message_id,inline_keyboard)

        # except:
        #     pass
            # m_data.list_admin[f"{m_data.users[f'{message.chat.id}']['username']}"] = False
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